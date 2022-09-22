import numpy as np
import matplotlib.pyplot as plt

a = np.array([0,-9.81])
v = np.array([np.cos(np.deg2rad(40)) * 10, np.sin(np.deg2rad(40)) * 10])
v1 = v
s = np.array([0,5])

t = 0
dt = 0.01
y_landing = 0

vl = [[],[]]
sl = [[],[]]
tl = []

while s[1] > 0:
    v = v + a * dt
    vl[0].append(v[0])
    vl[1].append(v[1])
    s = s + v * dt
    sl[0].append(s[0])
    sl[1].append(s[1])
    t = t + dt
    tl.append(t)

print(f'startfart: {v1}')

print(f'tid: {t}')

print(f'avstand fra tårn: {s[0]}')

print(f'farstvektor: {v}')

print(f'fart: {np.linalg.norm(v)}')

plt.plot(sl[0],sl[1])