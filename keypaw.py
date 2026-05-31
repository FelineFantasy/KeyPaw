import os
import sys
import keyboard
from pygame import mixer

mixer.init()

do = mixer.Sound('notes/do.wav')
re = mixer.Sound('notes/re.wav')
mi = mixer.Sound('notes/mi.wav')
fa = mixer.Sound('notes/fa.wav')
sol = mixer.Sound('notes/sol.wav')
lja = mixer.Sound('notes/lja.wav')
si = mixer.Sound('notes/si.wav')

keymap = {
    "1": do,
    "2": re,
    "3": mi,
    "4": fa,
    "5": sol,
    "6": lja,
    "7": si,
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
    
    if event.name in keymap:
        keymap[event.name].play()
    
    return False

keyboard.hook(handle_key)

os.system('cls' if os.name == 'nt' else 'clear')
print("Пианино готово! Нажимай цифры 1-7.")
print("Нажми ESC для выхода.")

while running:
    pass

keyboard.unhook_all()
mixer.quit()
