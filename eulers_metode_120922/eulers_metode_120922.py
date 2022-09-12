import numpy as np
import matplotlib.pyplot as plt


# Skal simulere et ballkast MED luftmotstand med Eulers metode , og tegne grafer

# Definerer konstanter
dt = 0.01  #Tidssteg i sekunder.

T = 5.0    # Hvor mange sekunder vi vil simulere
m = 0.5     # Massen trengs for luftmotstand
k = 0.1     # Friksjonstall
g = -9.81

#Definerer startverdier i lister.
s = [1.0]   #Startposisjon 
v = [10.0]     #Startfart
t = [0.0]    # Starttid
a = [g - k * abs(v[0]) * v[0] / m]     # Akselerasjonen varierer pga luftmotstanden L = kv^2 

#En løkke fungerer som en tikkende klokke.
#For hvert tikk regner vi ut ny fart og posisjon.
i= 0
while t[i] < T:
    L = k * abs(v[i]) * v[i]
    Fsum = m * g - L
    a.append(Fsum / m)
    s.append(s[i] + v[i]*dt)
    v.append(v[i] + a[i]*dt)
    t.append(t[i] + dt)
    i = i+1
  
  
plt.figure(1)
plt.title("Ballkast rett opp")
plt.plot(t, s, 'r', label="Posisjon med L")
plt.grid()
plt.xlabel("Tid / s")
plt.ylabel("Posisjon / m")
plt.legend()
plt.show()
plt.title("Ballkast rett opp")
plt.plot(t, v, 'r', label="Fart med L")
plt.grid()
plt.xlabel("Tid / s")
plt.ylabel("Fart / m/s")
plt.legend()
plt.show()
plt.title("Ballkast rett opp")
plt.plot(t, a, 'r', label="Aks med L")
plt.grid()
plt.xlabel("Tid / s")
plt.ylabel("Aks / m/s^2")
plt.legend()
plt.show()
