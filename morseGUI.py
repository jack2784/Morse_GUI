from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)

red = LED(27)

win = Tk()
win.title("Morse Code")
myfont = tkinter.font.Font(family = "helvetica", size = 12, weight = "bold")


CODE = {'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',}


def runMorseCode():
    red.off()
    if(len(text.get()) > 12):
        print("text too long")
        print(text.get())
    else:
        print(text.get())
        for letter in text.get():
                for symbol in CODE[letter.upper()]:
                    if symbol == '-':
                        dash()
                    elif symbol == '.':
                        dot()
                    else:
                        time.sleep(0.5)
                time.sleep(1.5)

def dash():
    red.on()
    time.sleep(1)
    red.off()
    time.sleep(0.5)

def dot():
    red.on()
    time.sleep(0.3)
    red.off()
    time.sleep(0.5)

def quitwin():
    red.off()
    win.destroy()

Label(win, text="Text to convert:").grid(row=0)
text = Entry(win)
text.grid(row=0, column=1)


redbutton = Button(win, text = "Run Morse Code", font = myfont, command = lambda: runMorseCode(), bg = "bisque2", height = 1, width = 24)
redbutton.grid(row=1,column=1)

offbutton = Button(win, text = "Quit", font = myfont, command = lambda: quitwin(), bg = "bisque2", height = 1, width = 24)
offbutton.grid(row=2,column=1)
