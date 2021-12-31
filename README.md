# DISCLAIMER

I don't know music theory, which implies that there may be inaccuracies in the conversion from MusicXML to simplified abc notation.

# MusicXML to simplified abc notation

Tool to convert MusicXML file into a simplified abc notation.

## Simplified abc notation syntax

General syntax: `[note][duration]`

### Note

#### Natutal notes

`[pitch step lowercase][pitch octave]`

#### Sharp notes

`[pitch step UPPERCASE][pitch octave]`

#### Flat notes

Flat notes are converted into equivalent sharp notes.

#### Rest

`[-=]`

### Duration

The duration is calculated as <br>
![equation](https://latex.codecogs.com/gif.image?%5Cdpi%7B110%7D%20%5Clog_2%5Cleft(%5Cfrac%7B2%7D%7B%5Ctext%7BquarterLength%7D%7D%5Cright)) <br>
so that it represents an index of an array with the following structure: `[1,1/2,1/4,1/8,1/16,...]`

## Installation
Install all dependencies:
```
pip install -r ./requirements.txt
```

## Example
**Source (example.xml)**
![image](https://user-images.githubusercontent.com/40419916/147823619-016c78bd-0d34-405b-a077-aa7041c859a1.png)
```
> py main.py
Enter MusicXML file path: example.xml
d51 -=2 a42 d51 -=2 a42 d52 a42 d52 F52 a51 -=1 g51 -=2 e52 g51 -=2 e52 g52 e52 C52 e52 a41 -=1 d51 d50 F52 e52 d52 d52 C52 C50 e52 g52 C52 e52 d52 d50 F52 e52 d52 d52 C52 C50 e52 g52 C52 d52 d52 d53 C53 b43 C53 d52 d52 F53 e53 d53 
e53 F52 F52 a53 g53 F53 g53 a51 -=1
```
