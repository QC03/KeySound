

from SoundManager import SoundManager
from InputListener import InputListener

class MainApp:
    def __init__(self):
        self.sound_player = SoundManager()
        self.listener = InputListener(self.sound_player)

    def run(self):
        print("Press F9 to exit.")
        self.listener.start()

if __name__ == "__main__":
    app = MainApp()
    app.run()