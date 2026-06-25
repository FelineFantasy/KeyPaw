import os
import keyboard
import pygame
import time

pygame.mixer.init()

do = pygame.mixer.Sound('notes/do.wav')
re = pygame.mixer.Sound('notes/re.wav')
mi = pygame.mixer.Sound('notes/mi.wav')
fa = pygame.mixer.Sound('notes/fa.wav')
sol = pygame.mixer.Sound('notes/sol.wav')
lja = pygame.mixer.Sound('notes/lja.wav')
si = pygame.mixer.Sound('notes/si.wav')

notes = {
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
    if event.name in notes:
        notes[event.name].play()
    return False

keyboard.hook(handle_key)

os.system('cls' if os.name == 'nt' else 'clear')
print("KeyPaw готово! Нажимай 1-7.")
print("Нажми ESC для выхода.")

while running:
    time.sleep(0.1)

keyboard.unhook_all()
pygame.mixer.quit()
