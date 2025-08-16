
import Sound_Manager
from pynput import keyboard, mouse

class inputListener:

    def __init__(self, player: Sound_Manager):
        self.player = player
        self.keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        self.mouse_listener = mouse.Listener(on_click=self.on_click)

    def on_key_press(self, key):
        print(f"키 입력: {key}")
        self.player.play_sound("key")

    def on_click(self, x, y, button, pressed):
        if pressed:
            print(f"마우스 클릭: {button} at ({x}, {y})")
            self.player.play_sound("click")

    def start(self):
        self.keyboard_listener.start()
        self.mouse_listener.start()
        self.keyboard_listener.join()
        self.mouse_listener.join()