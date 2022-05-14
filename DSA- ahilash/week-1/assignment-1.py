arr=input().split()
res={}
for i in arr:
    if (i in res.keys()):
        res[i] += 1
    else:
        res[i]= 1
print (res, "=========> result")