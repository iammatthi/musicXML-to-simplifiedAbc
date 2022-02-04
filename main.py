from music21 import *
import math


def getDurationIndex(el):
    return max(0, int(math.log2(4 / el.duration.quarterLength)))


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
        octave = el.pitch.octave
        if el.pitch.accidental is not None and el.pitch.accidental.modifier == "#":
            # sharp note
            if el.pitch.step == "B":
                # convert B#x to C(x+1)
                step = "c"
                octave += 1
            else:
                step = el.pitch.step
        elif el.pitch.accidental is not None and el.pitch.accidental.modifier == "-":
            # flat note
            # normalize to equivalent sharp note
            step = el.pitch.transpose(-1).step
        else:
            # natural note or without accidental
            step = el.pitch.step.lower()

        duration = getDurationIndex(el)

        result += f"{step}{octave}{duration} "
    elif el.isRest:
        duration = getDurationIndex(el)
        result += f"-={duration} "
    else:
        print("UNKNOWN ELEMENT", el)
        exit(1)


print(result)
