from pathlib import Path

import FileReader as fr
import Plotter as p
import Types


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

    l.sort(reverse=True, key=p.graphableSorter)
    p.showSubplotBarChart(l)