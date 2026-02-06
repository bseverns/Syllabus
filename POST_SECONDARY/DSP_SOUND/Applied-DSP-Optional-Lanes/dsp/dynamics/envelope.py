import math

class Envelope:
    def __init__(self, sr, attack_ms=10.0, release_ms=100.0):
        self.sr=float(sr)
        self.set_times(attack_ms, release_ms)
        self.env=0.0

    def set_times(self, attack_ms, release_ms):
        a=max(0.1, float(attack_ms))/1000.0
        r=max(0.1, float(release_ms))/1000.0
        self.a = math.exp(-1.0/(a*self.sr))
        self.b = math.exp(-1.0/(r*self.sr))

    def process(self, x):
        x=abs(float(x))
        if x>self.env:
            self.env = (1-self.a)*x + self.a*self.env
        else:
            self.env = (1-self.b)*x + self.b*self.env
        return self.env
