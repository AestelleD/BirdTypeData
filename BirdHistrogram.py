import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
##Import Dependencies^^
plt.xlabel('Birds Recorded')
plt.ylabel('Number of Recordings')
plt.title("Frequency of Recording Values VS Number of Birds Recorded")
##Setup Graph Title and labels^^
data_Filename = input("Input Filename here, no .json")
f = open( data_Filename + '.json')
data = json.load(f)
## Loads The .json file
valuedict = {} ## Empty Dictonary of Values
for i in data:
    valuedict[(i["name"])] = int((i["count"]))
## Create dictonary of the values, matching the name to the count of birds
print(valuedict) ##prints the value
for key, value in list(valuedict.items()):  ##removes all the values under 5 or above 49 
    if int(value) < 5:
        del valuedict[key]
    if int(value) > 49:
        del valuedict[key]      
print(valuedict) ##prints the dictonary of values
xv = list(valuedict.keys())  ##sets x values to the keys
yv = list(valuedict.values()) ## sets x values to the values
plt.hist(yv,ec="k") ##Sets plot as a histogram, ec=k is something about color idk i stole this part
plt.show() ##Shows the plot




##Extra stuff that was in the program that i got rid of 
#xvalues = []  ##Empty Set for x and y values
#yvalues = []

#vd2={}
#for i in data:
   # print(i["date"])
 #   xvalues.append(i["name"])
#for i in data:
   # print(i["count"])
 #   yvalues.append(int(i["count"]))

#print(xvalues)
#print(yvalues)
#plt.xlim(0,(60))
#plt.ylim(0,(10))

    #print(value)

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