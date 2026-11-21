import pytest

class Pixel:
    def __init__(self, duration):
        self.log = []
        global log
        log = self.log
        self.color = (0, 0, 0)
        self.history = []
        self.duration = duration

        global pix
        pix = self

    def test_fake_sleep(self, t):
        self.log.append(t)

    def fill(self, color):
        self.history.append((self.color, len(self.log)))
        self.color = color

    def look(self):
        # Temporary copy of history
        cur_history = self.history[::]
        if self.duration >= 0:
            if len(set(self.log)) != 1 or self.duration != pytest.approx(self.log[0], 0.001):
                log = self.log[::]
                self.log.clear()
                return (False, (self.duration, log))
        cur_history.append((self.color, len(self.log)))
        self.log.clear()
        return (True, (self.color, cur_history))
