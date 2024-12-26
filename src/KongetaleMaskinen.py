from pathlib import Path

OccurrenceDict = dict[str, int]
YearOccurrenceDictContainer = dict[int, dict[str, int]]
SpeechDict = dict[int, Path]

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

def textToOccurrenceDict(text: str) -> OccurrenceDict:
    # Split text and save in dict
    d:OccurrenceDict = OccurrenceDict()
    for word in cleanText(text).split(' '):
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    return d

def filesToOccurrencesDictionaries(pathDict: SpeechDict) -> YearOccurrenceDictContainer:
    d:YearOccurrenceDictContainer = YearOccurrenceDictContainer()
    for key in pathDict:
        s:str = readFromFile(pathDict[key])
        s = cleanText(s)
        d[key] = textToOccurrenceDict(s)
    return d

if __name__ == "__main__":
    d = SpeechDict()
    d[2012] = Path('speeches/2012.txt')
    d[2022] = Path('speeches/2022.txt')
    print(filesToOccurrencesDictionaries(d))