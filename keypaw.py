#!/usr/bin/env python3

import os
import keyboard
import pygame
import time

pygame.mixer.init()

note_names = ['do', 're', 'mi', 'fa', 'sol', 'lja', 'si']
notes = {}

for i, name in enumerate(note_names, 1):
    try:
        notes[str(i)] = pygame.mixer.Sound(f'notes/{name}.wav')
    except FileNotFoundError:
        print(f"Ошибка: файл notes/{name}.wav не найден!")
        pygame.mixer.quit()
        exit(1)

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
