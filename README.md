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

The duration is calculated as <br>
![equation](https://latex.codecogs.com/gif.image?%5Cdpi%7B110%7D%20%5Clog_2%5Cleft(%5Cfrac%7B2%7D%7B%5Ctext%7BquarterLength%7D%7D%5Cright)) <br>
so that it represents an index of an array with the following structure: `[1,1/2,1/4,1/8,1/16,...]`
