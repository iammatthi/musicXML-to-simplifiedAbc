# DISCLAIMER

I don't know music theory, which implies that there may be inaccuracies in the conversion from MusicXML to simplified abc notation.

# MusicXML to simplified abc notation

Tool to convert MusicXML into a simplified abc notation.

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
$$\log_2 \left( \frac{4}{\text{quarterLength}} \right)$$
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
d52 -=3 a43 d52 -=3 a43 d53 a43 d53 F53 a52 -=2 g52 -=3 e53 g52 -=3 e53 g53 e53 C53 e53 a42 -=2 d52 d51 F53 e53 d53 d53 C53 C51 e53 g53 C53 e53 d53 d51 F53 e53 d53 d53 C53 C51 e53 g53 C53 d53 d53 d54 C54 b44 C54 d53 d53 F54 e54 d54 e54 F53 F53 a54 g54 F54 g54 a52 -=2
```
