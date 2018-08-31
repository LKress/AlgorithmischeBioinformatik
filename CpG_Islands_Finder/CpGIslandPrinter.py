from matplotlib import pyplot as plot


# This part of the program was used from the Software Engineering Project "OpenTemperature"
# and was originally written by Johannes Hausmann but changed for this project
def draw(name, fileName, frameLength):
    plot.figure()

    plot.xlabel('Frame')
    plot.ylabel('Log-Likelihood-Ratio')
    plot.title("CpG Islands ({}-Baselong frames)".format(frameLength))

    plot.grid()
    plot.plot(name, color='r', linewidth=1.0)
    plot.savefig('./{}'.format(fileName))
