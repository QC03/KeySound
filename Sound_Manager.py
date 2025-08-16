
import pygame

class soundManager:

    def __init__(self):
        pygame.mixer.init()  # 오디오 초기화
        self.sounds = {
            "key": pygame.mixer.Sound("sounds/key.wav"),
            "click": pygame.mixer.Sound("sounds/click.wav")
        }

    def play_sound(self, name: str):
        if name in self.sounds:
            # pygame은 비동기 재생 지원 → 따로 스레드 필요 없음
            self.sounds[name].play()