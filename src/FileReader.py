from pathlib import Path
import Types

def readFromFile(path: Path) -> str:
    # Todo: check if file exists and can be opened
    return path.open().read()

def cleanText(text:str) -> str:
    #Remove dots, commas and newlines.
    text = text.replace('.','')
    text = text.replace(',','')
    text = text.replace('\n','')
    text = text.lower()
    return text

def textToOccurrenceDict(text: str) -> Types.OccurrenceDict:
    # Split text and save in dict
    d:Types.OccurrenceDict = Types.OccurrenceDict()
    for word in cleanText(text).split(' '):
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    return d

def filesToOccurrencesDictionaries(pathDict: Types.SpeechDict) -> Types.YearOccurrenceDictContainer:
    d:Types.YearOccurrenceDictContainer = Types.YearOccurrenceDictContainer()
    for key in pathDict:
        s:str = readFromFile(pathDict[key])
        s = cleanText(s)
        d[key] = textToOccurrenceDict(s)
    return d

def getGraphable(word:str, allOccurrences:Types.YearOccurrenceDictContainer) -> Types.Graphable:
    g:Types.Graphable = Types.Graphable()
    g.word = word

    o:Types.Occurrences = Types.Occurrences()
    lowerWord:str = word.lower()

    for key in allOccurrences:
        if not lowerWord in allOccurrences[key]:
            o[key] = 0
        else:
            o[key] = allOccurrences[key][lowerWord]

    g.occurrences = o
    return g