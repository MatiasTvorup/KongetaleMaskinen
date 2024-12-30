from pathlib import Path

OccurrenceDict = dict[str, int]
YearOccurrenceDictContainer = dict[int, dict[str, int]]
SpeechDict = dict[int, Path]
Occurrences = dict[int, int]

class Point:
    x:int = 0
    y: int = 0

class Graphable:
    word:str = ""
    threshold:float = 0
    occurrences:Occurrences= Occurrences()

    def IsValid(self) -> bool:
        return self.word != "" and self.threshold != 0 and bool(self.occurrences)
    
    def Certainty(self) -> float:
        overThreshholdCount:int = 0
        underThreshholdCount: int = 0

        for key in self.occurrences:
            if(self.occurrences[key] > self.threshold):
                overThreshholdCount += 1
            else:
                underThreshholdCount += 1
        
        return max(overThreshholdCount, underThreshholdCount) / (overThreshholdCount + underThreshholdCount) * 100
    
    def BetOn(self) -> str:
        overThreshholdCount:int = 0
        underThreshholdCount: int = 0

        for key in self.occurrences:
            if(self.occurrences[key] > self.threshold):
                overThreshholdCount += 1
            else:
                underThreshholdCount += 1

        if(overThreshholdCount > underThreshholdCount):
            return "Over"
        elif(overThreshholdCount < underThreshholdCount):
            return "Under"
        else:
            return "???"
