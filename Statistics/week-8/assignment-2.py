import statsmodels.api as sm
from statsmodels import tsa as TSA
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.ar_model import AutoReg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def MSE(arr):
    MSE = 0
    for i in range(0, len(arr)):
        MSE += arr[i] * arr[i]
    return MSE


def EACF(arma, ar_max, ma_max, show):
    def lag1(arma, lag=1):
        return pd.Series(arma).shift(lag)

    def reupm(m, nrow, ncol):
        k = ncol - 1
        m2 = np.empty((m.shape[0], k))
        for i in range(k):
            i1 = i + 1
            work = lag1(m1[:, i])
            work[0] = -1
            temp = m1[:, i1] - work * m1[i1, i1]/m1[i, i]
            temp[i1] = 0
            m2[:, i] = temp
        return m2

    def ceascf(m, cov1, nar, ncol, count, ncov, arma, armam):
        result = np.zeros(nar+1)
        result[0] = cov1[ncov + count - 1]
        for i in range(1, nar+1):
            A = np.empty((len(arma) - i, i+1))
            A[:, 0] = arma[i:]
            A[:, 1:] = armam[i:, :i]
            b = np.r_[1, -m[:i, i-1]]
            temp = A @ b
            result[i] = acf(temp, nlags=count, fft=False)[count]
        return result

    ar_max = ar_max + 1
    ma_max = ma_max + 1
    nar = ar_max - 1
    nma = ma_max
    ncov = nar + nma + 2
    nrow = nar + nma + 1
    ncol = nrow - 1
    arma = np.array(arma) - np.mean(arma)
    armam = np.empty((len(arma), nar))
    for i in range(nar):
        armam[:, i] = lag1(arma, lag=i+1)
    cov1 = acf(arma, nlags=ncov, fft=False)
    cov1 = np.r_[np.flip(cov1[1:]), cov1]
    ncov = ncov + 1
    m1 = np.zeros((nrow, ncol))
    for i in range(ncol):
        m1[:i+1, i] = AutoReg(arma, lags=i+1, trend='c').fit().params[1:]

    eacf = np.empty((ar_max, nma))
    for i in range(nma):
        m2 = reupm(m=m1, nrow=nrow, ncol=ncol)
        ncol = ncol - 1
        eacf[:, i] = ceascf(m2, cov1, nar, ncol, i+1, ncov, arma, armam)
        m1 = m2

    work = np.arange(1, nar+2)
    work = len(arma) - work + 1
    symbol = np.empty(eacf.shape, dtype=object)
    for i in range(nma):
        work = work - 1
        symbol[:, i] = np.where(np.abs(eacf[:, i]) > 2/np.sqrt(work), 'x', 'o')

    symbol = pd.DataFrame(symbol)
    if show:
        print('AR / MA')
        print(symbol)

    return {
        'eacf': eacf,
        'ar.max': ar_max,
        'ma.max': ma_max,
        'symbol': symbol
    }


df_robot = pd.read_csv("TSA HW06.robot.csv")


plt.plot(df_robot)

# acf
data_acf = TSA.stattools.acf(df_robot, nlags=40, fft=False)
print("ACF of the data:\n", data_acf, "\n")
plt.plot(data_acf, "bD", linestyle='dashed')
sm.graphics.tsa.plot_acf(df_robot, lags=100)
plt.show()

# pacf
data_pacf = TSA.stattools.pacf(df_robot, nlags=40)
print("PACF of the data:\n", data_pacf, "\n")
plt.plot(data_pacf, "bD", linestyle='dashed')
sm.graphics.tsa.plot_pacf(df_robot, lags=100)
plt.show()


result_EACF = EACF(df_robot.iloc[:, 0], 5, 5, True)
print('\n\n ECAF Matrix: \n', np.around(result_EACF['eacf'], decimals=4))

# AR(1)
model_AR1 = AutoReg(df_robot, lags=1)
model_AR1_fit = model_AR1.fit()
print("AR(1) Model:\n", model_AR1_fit.params)
print(model_AR1_fit.summary())

#IMA(1, 1)
model_IMA = ARIMA(df_robot, order=(0, 1, 1))
model_IMA_fit = model_IMA.fit()
print("\n\nIMA(1,1) Model:\n", model_IMA_fit.params)
print(model_IMA_fit.summary())


print("AIC of AR(1) model", model_AR1_fit.aic)

print("\n\nAIC of IMA(1, 1) model", model_IMA_fit.aic, "\n\n\n")

# residual test
predict_AR = model_AR1.predict(start=0, end=(
    len(df_robot)), params=model_AR1_fit.params).tolist()
predict_IMA = model_IMA_fit.predict(params=model_IMA_fit.params).tolist()

for i in range(len(df_robot)):
    df_robot.loc[i, 'residual_AR'] = predict_AR[i] - df_robot['robot'][i]
    df_robot.loc[i, 'residual_IMA'] = predict_IMA[i] - df_robot['robot'][i]

df_robot.loc[:, 'residual_AR']
plt.plot()
df_robot.loc[:, 'residual_IMA']
plt.plot()
plt.show()

MSE(df_robot['residual_AR'])
MSE(df_robot['residual_IMA'])
