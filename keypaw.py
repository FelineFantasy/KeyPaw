import os
import sys
import keyboard
from musicpy import *

notes = {
    "1": C4,
    "2": D4,
    "3": E4,
    "4": F4,
    "5": G4,
    "6": A4,
    "7": B4,
    "!": Cs4,
    "@": Ds4,
    "$": Fs4,
    "%": Gs4,
    "^": As4,
    "q": C5,
    "w": D5,
    "e": E5,
    "r": F5,
    "t": G5,
    "y": A5,
    "u": B5,
}

running = True

def handle_key(event):
    global running
    
    if event.event_type != 'down':
        return False
    
    if event.name == 'esc':
        print("\nВыход из пианино...")
        running = False
        return False
    
    if event.name in notes:
        play(notes[event.name], duration=0.5, wait=False)
    
    return False

keyboard.hook(handle_key)

os.system('cls' if os.name == 'nt' else 'clear')
print("Пианино готово! Нажимай клавиши:")
print("1-7 — обычные ноты")
print("Shift+1,2,4,5,6 — диезы")
print("q-w-e-r-t-y-u — вторая октава")
print("Нажми ESC для выхода.")

while running:
    pass

keyboard.unhook_all()
