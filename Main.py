import MarkovMatrixCalculator as mmc
import LogLikelihoodCalculator as llc
import CpGIslandPrinter as cip

print("#---------------------------#\n" +
      "#     CpG Island Finder     #\n" +
      "#---------------------------#\n")
CpGFileName = input("Enter the name of a CpG file for calculating the positive Matrix:\n")

mmc.createPreparedTextFile(CpGFileName)
plusMatrix = mmc.calculateAMatrix(mmc.countPairs())
mmc.deletePreparedTextFile()
mmc.printArray(plusMatrix)
print()

backgroundFileName = input("Enter the name of a background file for calculating the negative Matrix:\n")

mmc.createPreparedTextFile(backgroundFileName)
minusMatrix = mmc.calculateAMatrix(mmc.countPairs())
mmc.deletePreparedTextFile()
mmc.printArray(minusMatrix)
print()

searchFileName = input("For searching CpG islands enter the name of the search file:\n")

mmc.createPreparedTextFile(searchFileName)
resArray = llc.calculateLogLikeRatio(plusMatrix, minusMatrix, searchFileName, 51)

resArray1 = llc.calculateLogLikeRatio(plusMatrix, minusMatrix, searchFileName, 201)

resArray2 = llc.calculateLogLikeRatio(plusMatrix, minusMatrix, searchFileName, 401)

mmc.deletePreparedTextFile()

cip.draw(resArray, "frame51.png", "51")

cip.draw(resArray1, "frame201.png", "201")

cip.draw(resArray2, "frame401.png", "401")

