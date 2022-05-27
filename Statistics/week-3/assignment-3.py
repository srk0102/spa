import numpy as np

if __name__ == "__main__":
    print("COURSE NAME: ")
    print("NAME: ")
    print( "PROGRAMMING ASSIGNMENT #3 \n")


train_csv = 'iris-training-data.csv'
test_csv = 'iris-testing-data.csv'

# gather necessary data
train_data = np.loadtxt(train_csv, delimiter = ",", usecols = (0, 1, 2, 3))
train_classes = np.loadtxt(train_csv, delimiter = ",", usecols = (4,),
                           dtype = str)
test_data = np.loadtxt(test_csv, delimiter = ",", usecols = (0, 1, 2, 3))
test_classes = np.loadtxt(test_csv, delimiter = ",", usecols = (4,),
                          dtype = str)
predicted_classes = []

#Function to find euclidean distance
def distance(x, y):
    return np.sqrt(np.sum((x-y)**2))

for row in test_data:
    # find distance between this row and every row in training
    distances = [distance(row, x) for x in train_data]
    predicted_class = np.argmin(distances) 
    predicted_classes.append(train_classes[predicted_class])

accuracy = ((sum(predicted_classes == test_classes) / float(test_classes.shape[0])) 
                * 100)

print("#, True, Predicted")

for x, y, z in zip(range(1, 76), test_classes, predicted_classes):
    print(x, y, z)
    
print("Accuracy: %f%% " % accuracy)
