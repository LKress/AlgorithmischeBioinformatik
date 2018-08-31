import os
import numpy

# hash Map for simpler access
baseHash = {"A": 0, "C": 1, "G": 2, "T": 3}

def createPreparedTextFile(filename):
    # deleting first row of the file
    os.system("cp {} changedFile.tmp".format(filename, filename))
    os.system("tail -n +2 changedFile.tmp > 'Base.tmp' && mv 'Base.tmp' changedFile.tmp")

    # deleting linebreaks
    os.system("tr -d '\n' < changedFile.tmp > changedFile.tmp.tmp")
    os.system("cp changedFile.tmp.tmp changedfile.tmp && rm changedFile.tmp.tmp")

def deletePreparedTextFile():
    os.system("rm changedFile.tmp")

def countPairs():
    file = open("changedFile.tmp", "r")
    baseMatrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    # saving the first element of the basePair
    zw = file.read(1)
    # get the length of the whole file
    count = len(open("changedFile.tmp", "r").read())
    # stop one infront of the last base because of checking in pairs
    for i in range(int(count-1)):
        zw2 = file.read(1)
        # increment match in the array
        baseMatrix[baseHash[zw]][baseHash[zw2]] = baseMatrix[baseHash[zw]][baseHash[zw2]] + 1
        zw = zw2
    file.close()
    return baseMatrix

def printArray(array):
    # print the array
    for i in range(len(array)):
        for j in range(len(array[i])):
            print("{0:.2f}".format(array[i][j]), end=" ")
        print()

def calculateAMatrix(baseMatrix):
    # creating the Matrix with the chances
    calculatedMatrix = numpy.empty((4, 4))
    for i in range(4):
        allPairsOneRow = 0
        # Sum of one row of baseMatrix
        for k in range(4):
            allPairsOneRow = allPairsOneRow + baseMatrix[i][k]
        # dividing
        for j in range(4):
            calculatedMatrix[i][j] = baseMatrix[i][j] / allPairsOneRow
    return calculatedMatrix
