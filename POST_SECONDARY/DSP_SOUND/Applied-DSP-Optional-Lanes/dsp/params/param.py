from dataclasses import dataclass
import math

def clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x

@dataclass
class Param:
    name: str
    lo: float
    hi: float
    default: float
    smoothing: float = 0.15  # EMA alpha
    taper: str = "linear"    # linear|expo|log
    _target: float = None
    _value: float = None

    def __post_init__(self):
        self._target = float(self.default)
        self._value = float(self.default)

    def set_target(self, v: float):
        self._target = clamp(float(v), self.lo, self.hi)

    def set_normalized(self, x01: float):
        x01 = clamp(float(x01), 0.0, 1.0)
        if self.taper == "linear":
            v = self.lo + x01 * (self.hi - self.lo)
        elif self.taper == "expo":
            k = 3.0
            v = self.lo + (x01 ** k) * (self.hi - self.lo)
        elif self.taper == "log":
            k = 9.0
            v = self.lo + (math.log1p(k * x01) / math.log1p(k)) * (self.hi - self.lo)
        else:
            raise ValueError("unknown taper")
        self.set_target(v)

    def tick(self) -> float:
        a = clamp(self.smoothing, 0.0, 1.0)
        self._value = a * self._target + (1.0 - a) * self._value
        return self._value

    @property
    def value(self) -> float:
        return float(self._value)
