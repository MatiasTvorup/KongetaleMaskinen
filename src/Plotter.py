import matplotlib.pyplot as plt
import Types



def subplotSize(count:int) -> Types.Point:
    p:Types.Point = Types.Point()

    plotCount:int = p.x * p.y

    while plotCount < count:
        p.x += 1
        
        plotCount = p.x * p.y
        if plotCount >= count:
            return p
        
        p.y += 1

        plotCount = p.x * p.y
        if plotCount >= count:
            return p

    return p

def showBarChart(word:str, occurrences:Types.Occurrences, threshold:float) -> None:
    xValues:list[int] = list(occurrences.keys())
    yValues:list[int] = list(occurrences.values())

    plt.bar(xValues, yValues)
    plt.title("Antal gange '" + word + "' er blevet nævnt")
    plt.xlabel("Årstal")
    plt.axhline(y=threshold,linewidth=1, color='r')
    plt.show()

def showSubplotBarChart(graphables:list[Types.Graphable]) -> None:
    gridSizes:Types.Point = subplotSize(len(graphables))
    fig, axs = plt.subplots(gridSizes.y, gridSizes.x)

    xgridSize = gridSizes.x - 1
    x:int = 0
    y:int = 0

    for graphable in graphables:
        if not graphable.IsValid():
            continue

        xValues:list[int] = list(graphable.occurrences.keys())
        yValues:list[int] = list(graphable.occurrences.values())

        axs[y,x].bar(xValues, yValues)
        axs[y,x].set_title(graphable.word + ": " + "{:.2f}".format(graphable.Certainty()) + "% " + graphable.BetOn())
        axs[y,x].axhline(graphable.threshold, color='m')
        axs[y,x].set_xticks(xValues)
        axs[y,x].set_xticklabels(xValues, rotation=-60)
        # axs[y,x].tick_params(rotation=-45)
        if(x == xgridSize):
            x = 0
            y +=1
        else:
            x += 1
    
    fig.tight_layout()

    plt.show()

def graphableSorter(graphable:Types.Graphable) -> float:
    return graphable.Certainty()
