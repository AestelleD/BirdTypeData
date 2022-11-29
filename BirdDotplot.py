import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np

plt.ylabel('# of Birds')
plt.xlabel('Date')
plt.title("Number of Birds Recorded VS Date")
f = open('data.json')
data = json.load(f)
xvalues = []
yvalues = []
valuedict = {}
vd2={}
for i in data:
   # print(i["date"])
    xvalues.append(i["date"])
for i in data:
   # print(i["count"])
    yvalues.append(int(i["count"]))
for i in data:
    valuedict[(i["date"])] = int((i["count"]))
print(valuedict)
for key, value in list(valuedict.items()):
    print(value)
    if int(value) < 5:
        del valuedict[key]
    if int(value) > 49:
        del valuedict[key]        
print(valuedict)
xv = list(valuedict.keys())
yv = list(valuedict.values())
#print(xvalues)
#print(yvalues)
#plt.xlim(0,(60))
#plt.ylim(0,(10))
plt.scatter(xv,yv)
m,b = np.polyfit(xv, yv, 1)
coef = np.polyfit(xv,yv,1)
poly1d_fn = np.poly1d(coef) 
plt.plot(xv, poly1d_fn(xv),"--k")
corr_matrix = np.corrcoef(yv, poly1d_fn(xv))
corr = corr_matrix[0,1]
R_sq = corr**2
print("The R^2 value of the chart is ", R_sq)
#print(m,b)
plt.show()
