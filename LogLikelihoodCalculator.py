import math

baseHash = {"A": 0, "C": 1, "G": 2, "T": 3}

# This part of the program was written with Johannes Hausmann
def calculateLogLikeRatio(baseMatrixPlus, baseMatrixMinus, nameOfFile, w):
    # write file into string
    file = open("changedFile.tmp", 'r')
    data = file.read()
    file.close()
    string = ''.join(data[1:])

    # get the length of the sequence for the loop
    lengthOfSequence = int(len(open("changedFile.tmp", "r").read()))
    #print(lengthOfSequence)

    resArray = []                            ####################################################
    for i in range(0, lengthOfSequence - w): # for loop modified by not jumping the framelength #
        resArray.append(0)                   ####################################################
        #print(i)
        for j in range(i, i + w - 1):
            resArray[len(resArray) - 1] += math.log10(baseMatrixPlus[baseHash[string[j]]][baseHash[string[j + 1]]] / baseMatrixMinus[baseHash[string[j]]][baseHash[string[j + 1]]])

    #print(resArray)
    return resArray

def printArray(array):
    print(array)
