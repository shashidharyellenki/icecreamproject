import csv
f = open("cleaned-cat-data-commma.csv", "r") #opens the file
orig = list(csv.reader(f))
data = [] #not label
test = []   #label
for line in orig:
    if line[0] != "Semester": # skip header
        # only include coded classes
        categories = line[7:10]
        if line[0] == "S21":
            test.append(categories)
        else:
            data.append(categories)

f.close()
# print("test: ",test)
# print("data: ",data)
#---------------------------
''''''
def predict(data, first, second, showWork=False):
    flavorProbs = { }
    allFlavors = getAllFlavors(data) # possible flavors
    # print("all flav: ", allFlavors)
    for flavor in allFlavors:
        flavorProb = getClassProb(data, flavor)
        firstProb = getCondProb(data, first, flavor, 0)
        # print("first:", first)
        # print("flavour1: ", flavor)
        secondProb = getCondProb(data, second, flavor, 1)
        # print("flavour2: ", flavor)
        # print("second:", second)
        overallProb = firstProb * secondProb * flavorProb
        flavorProbs[flavor] = overallProb
        if showWork:
             print(flavor,
             prob(overallProb), "-", prob(firstProb),
             prob(secondProb), prob(flavorProb))
    return bestGuess(flavorProbs) # find best value
   
    
def runDataset(modelData, testData):
    # print("modeldata: ",modelData)
    # print("testdata: ",testData)
    guessedRight = 0
    for line in testData:
        predictFav = predict(modelData, line[0], line[1])
        # print("line1:" ,line[0])
        # print("line2: ",line[1])
        # print("predictfac: ",predictFav)
        actualFav = line[2]
        # print("Actucalfac: ",actualFav)
        if predictFav == actualFav:
            guessedRight += 1
    # print("this is gussedright",guessedRight)
    # print("prob",guessedRight/len(testData))
        # print(len(testData))
    return round(guessedRight/len(testData),2)*100

    
    

def getClassProb(data, flavor):
  
    count = 0
    for line in data:
        # print(line[2])
        if line[2] == flavor:
            count += 1
    return count / len(data)

print(getClassProb(data, "other"))


# Probability that 1st/2nd favorite is X given that
# 3rd favorite is C. Load data from CSV.
def getCondProb(data, priorFlavor, thirdFlavor, priorIndex):
    count = 0
    total = 0
    for line in data:           
        if line[2] == thirdFlavor:          #line[2] checks in cat-3 [0,1,2]
            total += 1 # only count entries with third flavor
        
            if line[priorIndex] == priorFlavor:
                # print(line[priorIndex])
                count += 1
    # print(total, count)
    return count/total
# print(getCondProb(data, "other", "chocolate", 1))


#--------------------------------------------------------
'''this getflavours function will pic 6 flav from the data!'''
def getAllFlavors(data):
    allFlavors = [ ] #chocolate, fruit, cookie, other, vanilla, coffee
    # print(data.pop(0))
    for line in data:
        if line[2] not in allFlavors:
            allFlavors.append(line[2])
    return allFlavors
'''
1 []->fruit!in[] [fruit]
2[fruit]




'''

def bestGuess(flavorProbs):
    bestFlavor = None
    bestProb = -1       #doubt 0 or 1
    for flavor in flavorProbs:
        # print("flav",flavorProbs)
        # print("clubed",flavorProbs[flavor])
        # print("bestguess: ", flavor)
        if flavorProbs[flavor] > bestProb:
            bestProb = flavorProbs[flavor]
            # print("bestprob",bestProb)
            bestFlavor = flavor
            # print("bestflav", bestFlavor)
    return bestFlavor



def prob(num):
    return str(round(num*100, 2)) + "%" 


print(predict(data, "other", "fruit", showWork=True))
# print("TESTING RESULT:", runDataset(data, test))