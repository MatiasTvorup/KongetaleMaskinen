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
