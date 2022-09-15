import matplotlib.pyplot as plt

m = 1500
F = 1700
k = 3.2
T = 70
dt = 0.01
v = [0]
s = [0]
a = [F/m]
t = [0]



for i in range(int(T/dt)):
    L = k * v[i-1]**2
    a.append(F/m - L/m)
    v.append( (v[i] + dt * a[i-1]))
    t.append( t[i] + dt)



plt.figure(1)

plt.plot(t, v, 'r', label="Fart med L")
plt.grid()
plt.xlabel("Tid / s")
plt.ylabel("Fart / m/s")
plt.legend()
plt.show()
plt.plot(t, a, 'r', label="Aks med L")
plt.grid()
plt.xlabel("Tid / s")
plt.ylabel("Aks / m/s^2")
plt.legend()
plt.show()

v.sort()

print(f'maksimalfarten er {v[-1]}')

F= 0
for i in range(2,len(t)-2):
    p = ((v[i-1] * dt +dt* v[i+1]) / 2)
    s.append(p)
    F  = F +p
    
plt.plot(t[1:len(t)-2], s, 'r', label="Posisjon med L")
plt.grid()
plt.xlabel("Tid / s")
plt.ylabel("Posisjon / m")
plt.legend()
plt.show()