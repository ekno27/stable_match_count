import itertools

# retrieve data from txt file
with open('input1.txt') as textFile:
    fileInput = [line.split() for line in textFile]

# FUNCTIONS

#see if  possibleWife wants to stay with its assigned match
def checkPossibleWomansStays(possibleWife, currentMan, possibleWomansHusband):
    currentWoman = int(possibleWife)-1
    womanStays = True
    currentWomanPreferences = womenPreferenceList[currentWoman]
    
    if currentWomanPreferences.index(str(possibleWomansHusband)) <= currentWomanPreferences.index(str(currentMan+1)):
        womanStays = True
    else: 
        womanStays = False
    return womanStays

#see if currentMan wants to stay with its assigned match
def pairingIsStable(currentMan,currentWife, pairingTuple):
    currentMansPreferences = menPreferenceList[currentMan]
    pairingIsStable = True
    for possibleWife in currentMansPreferences:
        #if the currentWife is higher or equal to PossibleWife in the preference list 
        if currentMansPreferences.index(str(currentWife)) <= currentMansPreferences.index(str(possibleWife)):
            pairingIsStable = True
            break
        else: 
            possibleWomansHusband = pairingTuple.index(int(possibleWife)) + 1
            #check if possible woman wants to stay with her current husband
            if checkPossibleWomansStays(possibleWife, currentMan, possibleWomansHusband):
                pairingIsStable = True
            else:    
                pairingIsStable = False
                break
            
    return pairingIsStable

# Head function, params: a possible list of matches
def matchIsStable(pairingTuple):
    matchesAreStable = True
    currentMan = 0
    for currentWife in pairingTuple:
        if pairingIsStable(currentMan, currentWife, pairingTuple):
            matchesAreStable = True
        else:
            matchesAreStable = False
            break
        currentMan = currentMan + 1

    return matchesAreStable

#variables 
menPreferenceList = []
womenPreferenceList = []
numberOfPairs = int(fileInput[0][0])
stableMatches = 0

#organizing file inputs
count = 0
for item in fileInput:
    if count > 0:
        if count <= ((len(fileInput)-1)/2):
            menPreferenceList.append(item)
        else: 
            womenPreferenceList.append(item)
    count = count + 1

#creating array that will be used to create the permutations
possiblePairs = []
#count is one to match items in the file 
count = 1
for item in range(0, numberOfPairs):
    possiblePairs.append(count)
    count= count+1
permutationList = list(itertools.permutations(possiblePairs))

# running the algorithm
for pairingTuple in permutationList:
    if matchIsStable(pairingTuple):
        stableMatches = stableMatches + 1

print('Stable matches: %d' %stableMatches)