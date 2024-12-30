from pathlib import Path
import FileReader as fr

import Types

import matplotlib.pyplot as plt
import numpy as np

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
    fig, axs = plt.subplots(gridSizes.x, gridSizes.y)

    xgridSize = gridSizes.x - 1
    x:int = 0
    y:int = 0

    for graphable in graphables:
        if not graphable.IsValid():
            continue

        xValues:list[int] = list(graphable.occurrences.keys())
        yValues:list[int] = list(graphable.occurrences.values())

        axs[x,y].bar(xValues, yValues)
        axs[x,y].set_title(graphable.word + ": " + "{:.2f}".format(graphable.Certainty()) + "%")
        axs[x,y].axhline(graphable.threshold, color='m')
        axs[x,y].set_xticks(xValues)
        axs[x,y].tick_params(rotation=-45)
        if(x == xgridSize):
            x = 0
            y +=1
        else:
            x += 1
    
    fig.tight_layout()

    plt.show()

def graphableSorter(graphable:Types.Graphable) -> float:
    return graphable.Certainty()


if __name__ == "__main__":
    d = Types.SpeechDict()
    d[1998] = Path('speeches/1998.txt')
    d[1999] = Path('speeches/1999.txt')
    d[2000] = Path('speeches/2000.txt')
    d[2001] = Path('speeches/2001.txt')
    d[2002] = Path('speeches/2002.txt')
    d[2003] = Path('speeches/2003.txt')
    d[2004] = Path('speeches/2004.txt')
    d[2005] = Path('speeches/2005.txt')
    d[2006] = Path('speeches/2006.txt')
    d[2007] = Path('speeches/2007.txt')
    d[2008] = Path('speeches/2008.txt')
    d[2009] = Path('speeches/2009.txt')
    d[2010] = Path('speeches/2010.txt')
    d[2011] = Path('speeches/2011.txt')
    d[2012] = Path('speeches/2012.txt')
    d[2013] = Path('speeches/2013.txt')
    d[2014] = Path('speeches/2014.txt')
    d[2015] = Path('speeches/2015.txt')
    d[2016] = Path('speeches/2016.txt')
    d[2017] = Path('speeches/2017.txt')
    d[2018] = Path('speeches/2018.txt')
    d[2019] = Path('speeches/2019.txt')
    d[2020] = Path('speeches/2020.txt')
    d[2021] = Path('speeches/2021.txt')
    d[2022] = Path('speeches/2022.txt')
    d[2023] = Path('speeches/2023.txt')


    yearOccurrenceDict:Types.YearOccurrenceDictContainer = fr.filesToOccurrencesDictionaries(d)


    l:list[Types.Graphable] = list[Types.Graphable]()

    g:Types.Graphable = fr.getGraphable("Danmark", yearOccurrenceDict)
    g.threshold = 7.5
    l.append(g)

    g:Types.Graphable = fr.getGraphable("Danske", yearOccurrenceDict)
    g.threshold = 5.5
    l.append(g)

    g:Types.Graphable = fr.getGraphable("Tak", yearOccurrenceDict)
    g.threshold = 5.5
    l.append(g)

    g:Types.Graphable = fr.getGraphable("Verden", yearOccurrenceDict)
    g.threshold = 3.5
    l.append(g)

    g:Types.Graphable = fr.getGraphable("Nytår", yearOccurrenceDict)
    g.threshold = 2.5
    l.append(g)

    g:Types.Graphable = fr.getGraphable("Grønland", yearOccurrenceDict)
    g.threshold = 2.5
    l.append(g)

    g:Types.Graphable = fr.getGraphable("Færøerne", yearOccurrenceDict)
    g.threshold = 1.5
    l.append(g)

    g:Types.Graphable = fr.getGraphable("Samfund", yearOccurrenceDict)
    g.threshold = 1.5
    l.append(g)

    g:Types.Graphable = fr.getGraphable("Nytårsønsker", yearOccurrenceDict)
    g.threshold = 1.5
    l.append(g)

    l.sort(reverse=True, key=graphableSorter)


    showSubplotBarChart(l)