import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
## Imports needed dependencies^
plt.ylabel('# of Birds')
plt.xlabel('Date')
plt.title("Number of Birds Recorded VS Date")
filename_id = input("Filename")
f = open(filename_id + '.json')
data = json.load(f)
valuedict = {}
for i in data:
    valuedict[(i["date"])] = int((i["count"]))
print(valuedict)
for key, value in list(valuedict.items()):
    if int(value) < 5:
        del valuedict[key]
    if int(value) > 49:
        del valuedict[key]        
print(valuedict)
xv = list(valuedict.keys())
yv = list(valuedict.values())
plt.scatter(xv,yv)

m,b = np.polyfit(xv, yv, 1)
coef = np.polyfit(xv,yv,1)
poly1d_fn = np.poly1d(coef) 
plt.plot(xv, poly1d_fn(xv),"--k")
corr_matrix = np.corrcoef(yv, poly1d_fn(xv))
corr = corr_matrix[0,1]
R_sq = corr**2
print("The R^2 value of the chart is ", R_sq)
plt.show()

#####Extra Stuff 
#print(value)
#vd2={}
#for i in data:
    #print(i["date"])
#  #xvalues.append(i["date"])
#for i in data:
    #print(i["count"])
    #yvalues.append(int(i["count"]))
#print(xvalues)
#print(yvalues)
#plt.xlim(0,(60))
#plt.ylim(0,(10))
# #xvalues = []
#yvalues = []