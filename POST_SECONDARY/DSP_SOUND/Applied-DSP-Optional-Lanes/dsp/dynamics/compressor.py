import numpy as np
from .envelope import Envelope

def db(x):
    x = np.maximum(np.asarray(x, dtype=np.float32), 1e-12)
    return 20.0*np.log10(x)

def undb(d):
    return 10.0**(np.asarray(d, dtype=np.float32)/20.0)

class Compressor:
    def __init__(self, sr, threshold_db=-18.0, ratio=4.0, attack_ms=10.0, release_ms=100.0):
        self.sr=float(sr)
        self.th=float(threshold_db)
        self.r=float(ratio)
        self.env=Envelope(sr, attack_ms, release_ms)

    def process(self, buf):
        x=np.asarray(buf, dtype=np.float32)
        env=np.array([self.env.process(v) for v in x], dtype=np.float32)
        env_db=db(env)
        over = env_db - self.th
        gr_db = np.where(over>0.0, over*(1.0 - 1.0/self.r), 0.0)
        gain = undb(-gr_db)
        return x*gain, gr_db
