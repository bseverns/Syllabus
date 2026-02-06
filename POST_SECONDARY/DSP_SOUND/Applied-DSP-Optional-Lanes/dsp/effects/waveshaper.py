import numpy as np

def softclip(x):
    x = np.clip(x, -1.5, 1.5)
    return x - (x**3)/3.0

def tanhish(x):
    return np.tanh(x)

def process(buf, drive=1.0, mix=1.0, post=1.0, mode="tanh"):
    b = np.asarray(buf, dtype=np.float32)
    y = b * float(drive)
    y = tanhish(y) if mode=="tanh" else softclip(y)
    out = (1.0-float(mix))*b + float(mix)*y
    return out * float(post)
