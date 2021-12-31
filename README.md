# DISCLAIMER

I don't know music theory, which implies that there may be inaccuracies in the conversion from MusicXML to simplified abc notation.

# MusicXML to simplified abc notation

Tool to convert MusicXML file into a simplified abc notation.

## Simplified abc notation syntax

General syntax: `[note][duration]`

### Note

#### Natutal notes

`[pitch step lowercase][pitch octave][duration]`

#### Sharp notes

`[pitch step UPPERCASE][pitch octave][duration]`

#### Flat notes

Flat notes are converted into equivalent sharp notes.

#### Rest

`[-=][duration]`

### Duration

Duration is computed as
<img src="https://latex.codecogs.com/svg.image?\log_2\left(\frac{2}{\text{quarterLength}}\right)" title="\log_2\left(\frac{2}{\text{quarterLength}}\right)" />
so that it represent an index of an array with the following structure

` array = [1,1/2,1/4,1/8,1/16,...]`
