import csv
import matplotlib.pyplot as plt

def readData(filename):
    f = open(filename, "r")
    # Semester, 3 orig, 3 cleaned, 3 categories
    data = list(csv.reader(f))
    return data


def combineUncommon(d, cutoff):
    newD = { "other" : 0 }
    for flavor in d:
        if d[flavor] >= cutoff:
            newD[flavor] = d[flavor]
            print("this is d[flavor]: ",d[flavor])
        else:
            newD["other"] += d[flavor]
            print("this is d[flavor] in else : ",d[flavor])
    print(newD)
    return newD
  
def getIceCreamCounts(data):
    iceCreamDict = { }
    for i in range(1, len(data)): # skip header
        firstCol = data[0].index("#Flavour 1 (Cleaned data)") # only cleaned flavors
        for j in range(firstCol, firstCol+3):
            flavor = data[i][j]
            if flavor not in iceCreamDict:
                iceCreamDict[flavor] = 0
            iceCreamDict[flavor] += 1
    return iceCreamDict

data = readData("cleaned-cat-data-comma.csv")
d= getIceCreamCounts(data)
print(d)
# print("d;", d)
flavors = []
portions = []
for flavor in d:
    # print(flavor)
    flavors.append(flavor)
    portions.append(d[flavor])

# print("flav",flavors)
# print("port",portions)  #count coh=26

plt.pie(portions, labels=portions)
plt.show()