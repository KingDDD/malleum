#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

print ('Spring Mass Damper Program')

def Derivatives(State):
    m = 1.0
    c = 2.0
    k = 3.0
    ucontrol = 0.0
    A = np.asarray([[0.0,1.0],[-k/m,-c/m]])
    B = np.asarray([0.0,1.0/m])
    StateDot = np.dot(A,State) + B*ucontrol
    return StateDot;

#initializing state vector
State = np.asarray([1.0,-2.0])

#initialize Derivatives
StateDot = Derivatives(State)

#define time variables
tfinal = 10.0
tinitial = 0.0
timestep = 0.01
time = np.arange(tinitial, tfinal+timestep,timestep)

#create state array
StateOUT = np.zeros((2,len(time)))
for idx in range(0,len(time)):
    print 'Simulation ',time[idx]/tfinal*100,' Percent Complete'
    StateOUT[:,idx] = State
    StateDot = Derivatives(State)
    State += StateDot*timestep

#plot the data
position = StateOUT[0,:]
velocity = StateOUT[1,:]
plt.figure()
plt.subplot(121)
plt.plot(time,position)
plt.xlabel('Time (sec)')
plt.ylabel('Velocity (m/s)')
plt.grid()
plt.subplot(122)
plt.plot(time,velocity)
plt.xlabel("Time (sec)")
plt.ylabel('Velocity (m/s)')
plt.grid()
plt.show()
