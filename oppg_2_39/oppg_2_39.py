import numpy as np


a = np.array([0,-9.81])
v = np.array([np.cos(np.deg2rad(40)) * 10, np.sin(np.deg2rad(40)) * 10])
v1 = v
s = np.array([0,5])

t = 0
dt = 0.01
y_landing = 0

while s[1] > 0:
    v = v + a * dt
    s = s + v * dt
    t = t + dt

print(f'startfart: {v1}')

print(f'tid: {t}')

print(f'avstand fra tårn: {s[0]}')

print(f'farstvektor: {v}')

print(f'fart: {np.linalg.norm(v)}')