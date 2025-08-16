
from Sound_Manager import soundManager
from InputListener import inputListener

class main:

    def __init__(self):
        self.sound_player = soundManager()
        self.listener = inputListener(self.sound_player)

    def run(self):
        print("키보드/마우스 입력을 감지 중... (종료하려면 Ctrl+C)")
        self.listener.start()


if __name__ == "__main__":
    app = main()
    app.run()