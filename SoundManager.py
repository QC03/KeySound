

import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            "key": pygame.mixer.Sound("sounds/key.wav"),
            "click": pygame.mixer.Sound("sounds/click.wav")
        }

    def play_sound(self, name: str):
        if name in self.sounds:
            self.sounds[name].play()
