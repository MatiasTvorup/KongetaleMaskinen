
def cleanText(text:str) -> str:
    #Remove dots, commas and newlines.
    text = text.replace('.','')
    text = text.replace(',','')
    text = text.replace('\n','')
    text = text.lower()
    return text

def textToOccurrenceDict(text: str) -> dict[str, int]:

    # Split text and save in dict
    d = dict[str, int]()
    for word in cleanText(text).split(' '):
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    return d

if __name__ == "__main__":
    print(textToOccurrenceDict("Hej, hej hej... med dig,,dig"))