class Jauge():
    def __init__(self, max, step):
        self.min = 0
        self.value = 1
        self.max = max
        self.step = step

    def addValue(self, v):
        self.value += v
        if self.value > self.max:
            self.value = self.max
        elif self.value < self.min:
            self.value = self.min
