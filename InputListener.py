from pynput import keyboard, mouse
from SoundManager import SoundManager

class InputListener:
    def __init__(self, player: SoundManager):
        self.player = player

        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_key_press
        )
        self.mouse_listener = mouse.Listener(on_click=self.on_click)

    def on_key_press(self, key):

        # F9 => exit
        if (keyboard.Key.f9 == key):
            print("F9 detected. Exiting program...")
            self.stop()
            return False

        self.player.play_sound("key")

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.player.play_sound("click")

    def start(self):
        self.keyboard_listener.start()
        self.mouse_listener.start()
        self.keyboard_listener.join()
        self.mouse_listener.join()

    def stop(self):
        self.keyboard_listener.stop()
        self.mouse_listener.stop()
