from matplotlib import pyplot as plot


# This part of the program was used from the Software Engineering Project "OpenTemperature"
# and was originally written by Johannes Hausmann but changed for this project
def draw(name, fileName, frameLength):
    plot.figure(figsize=(19, 12))

    plot.xlabel('Frame')
    plot.ylabel('Log-Likelihood-Ratio')
    plot.title("CpG Islands ({}-Baselong frames)".format(frameLength))

    plot.grid()

    lineColor = 'r'

    if frameLength == "51":
        lineColor = 'g'
    if frameLength == "201":
        lineColor = 'b'
    plot.setp(plot.plot(name), color=lineColor, linewidth=1.0)

    plot.savefig('./{}'.format(fileName))
