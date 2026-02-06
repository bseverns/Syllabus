class DCBlock:
    def __init__(self, r=0.995):
        self.r = float(r)
        self.x1 = 0.0
        self.y1 = 0.0

    def process(self, x: float) -> float:
        y = x - self.x1 + self.r * self.y1
        self.x1 = x
        self.y1 = y
        return y
