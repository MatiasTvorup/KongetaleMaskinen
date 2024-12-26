from pathlib import Path
import FileReader as fr

import Types

import matplotlib.pyplot as plt
import numpy as np
import math


def showBarChart(word:str, occurrences:Types.Occurrences, threshold:float) -> None:
    xValues:list[int] = list(occurrences.keys())
    yValues:list[int] = list(occurrences.values())

    plt.bar(xValues, yValues)
    plt.title("Antal gange '" + word + "' er blevet nævnt")
    plt.xlabel("Årstal")
    plt.axhline(y=threshold,linewidth=1, color='r')
    plt.show()

def showSubplotBarChart(occurrenceDict:dict[str, Types.Occurrences]) -> None:
    gridSize:int = math.ceil(math.sqrt(len(occurrenceDict)))
    fig, axs = plt.subplots(gridSize, gridSize)

    gridSize -= 1
    x:int = 0
    y:int = 0

    for key in occurrenceDict:
        xValues:list[int] = list(occurrenceDict[key].keys())
        yValues:list[int] = list(occurrenceDict[key].values())

        axs[x,y].bar(xValues, yValues)
        if(x == gridSize):
            x = 0
            y +=1
        else:
            x += 1
    
    plt.show()


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
    # DanmarkOccurrance:Types.Occurrences = fr.getOccurrence("Danmark", yearOccurrenceDict)
    # showBarChart("Danmark", DanmarkOccurrance, 3.0)
    showSubplotBarChart({"danmark":fr.getOccurrence("Danmark", yearOccurrenceDict), "dansk":fr.getOccurrence("dansk", yearOccurrenceDict), "grønland":fr.getOccurrence("grønland",yearOccurrenceDict)})