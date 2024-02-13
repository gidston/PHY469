#Heat capacity of a solid using python

import numpy as np
import matplotlib.pyplot as plt

T0 = 500 #initial temperature of the solid
T_e = 300 #temperature of the environment

#Given parameters
k = 0.1 
A = 1
dt = 0.001
t_final = 100


#list to keep the results
t_list = [0]
T_list = [T_0]
#Heat_input = []

#Calculate the rate of heat transfer dQ/dt
def transfer_rate(T, T_e):
    return -k * A * (T - T_e) / d


for i in range(int(t_final/dt)):
    #update time
    t = (i + 1) * dt
    t_list.append(t)
    
    #heat change calculation 
    dQdt = transfer_rate(T_list[i - 1], T_e)
    T = T_list[-1] + dQdt * dt
    T_list.append(T)
    
    print('t = {:.2f}s; T = {:.3f}˚C; dQ(t) = {:.3f}J/s'.format(t, T, dQdt))
    
    
#Temperature Graph plotting
plt.plot(t_list, T_list)
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('A graph of Temperature of the Solid with respect to Time')
plt.grid(False)
plt.show()

# Calculation of Cp/V
Heat_input = np.linspace(0, max(T_list) - T_e, t_final)
temperature = np.zeros_like(Heat_input)
for i, Q in enumerate(Heat_input):
    T = Q + T_e
    temperature[i] = T
    
    #print(temperature[i])

#Temperature and heat graph plotting
plt.plot(Heat_input, temperature)
plt.xlabel('Heat Input (Q)')
plt.ylabel('Temperature (T)')
plt.title('A graph of Temperature against Heat Input')
plt.grid(False)
plt.show()