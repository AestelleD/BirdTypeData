import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np

plt.xlabel('Birds Recorded')
plt.ylabel('Number of Recordings')
plt.title("Frequency of Recording Values VS Number of Birds Recorded")
f = open('data.json')
data = json.load(f)
xvalues = []
yvalues = []
valuedict = {}
vd2={}
for i in data:
   # print(i["date"])
    xvalues.append(i["name"])
for i in data:
   # print(i["count"])
    yvalues.append(int(i["count"]))
for i in data:
    valuedict[(i["name"])] = int((i["count"]))
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
plt.hist(yv,ec="k")







#m,b = np.polyfit(xvalues, yvalues, 1)
#coef = np.polyfit(xvalues,yvalues,1)
##poly1d_fn = np.poly1d(coef) 
#plt.plot(xvalues, poly1d_fn(xvalues),"--k")
#corr_matrix = np.corrcoef(yvalues, poly1d_fn(xvalues))
#corr = corr_matrix[0,1]
#R_sq = corr**2
#print("The R^2 value of the chart is ", R_sq)
#plt.plot(xvalues)
#print(m,b)
plt.show()
