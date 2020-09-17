import time
from app import *
from openal import *
from util import *

source = None


class AudioSource:
    def __init__(self):
        oalInit()
        self.source = oalOpen(USE_AUDIO)

    def play(self, coordinate):
        X, Y, Z = coordinate
        self.source.set_position([float(X), float(Y), float(Z)])
        self.source.play()

        for _ in range(1):
            while self.source.get_state() == AL_PLAYING:
                time.sleep(0.2)
        # oalQuit()

    def xz_rotate(self):
        DEGREE = 0
        RADIUS = 2

        self.source.set_position([0, 0, RADIUS])
        self.source.play()

        for _ in range(6):
            while self.source.get_state() == AL_PLAYING:
                DEGREE += 13
                THETA = DEGREE * math.pi / 180
                self.source.set_position([RADIUS * math.sin(THETA), 0, RADIUS * math.cos(THETA)])
                time.sleep(0.2)
            self.source.play()


if __name__ == '__main__':
    a = App()
    a.set_widget()
    a.main_loop()
