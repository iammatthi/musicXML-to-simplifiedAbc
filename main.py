from music21 import *
import math


def getDurationIndex(el):
    return int(math.log2(2 / el.duration.quarterLength))


filePath = input("Enter MusicXML file path: ")
song = converter.parse(filePath, forceSource=True)
# process the ties
song = song.stripTies()

# unfold repetitions
i = 0
for a in song:
    if a.isStream:
        song[i] = repeat.Expander(a).process()
    i += 1

result = ""
for el in song.recurse().notesAndRests:
    if el.duration.isGrace:
        # ignore grace
        continue
    elif el.isNote:
        if el.pitch.accidental is not None and el.pitch.accidental.modifier == "#":
            # sharp note
            step = el.pitch.step
            if step == "B":
                # convert B# to C
                step = "c"
        elif el.pitch.accidental is not None and el.pitch.accidental.modifier == "-":
            # flat note
            # normalize to equivalent sharp note
            step = el.pitch.transpose(-1).step
        else:
            # natural note or without accidental
            step = el.pitch.step.lower()

        duration = getDurationIndex(el)

        result += f"{step}{el.pitch.octave}{duration} "
    elif el.isRest:
        duration = getDurationIndex(el)
        result += f"-={duration} "
    else:
        print("UNKNOWN ELEMENT", el)
        exit(1)


print(result)
