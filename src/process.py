#%% // Imports and initial setup
import serial
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

SAMPLES = 1000
CHANNELS = 3
DEADZONE = 15
VOLTAGE_THRESH = 50
read_data = np.zeros((CHANNELS,SAMPLES))
read_tof = np.zeros(CHANNELS)


#%% // Read data from serial
ser = serial.Serial('COM7', 9600)

ser.write(b'get\n')
for j in range(0, CHANNELS):
    for i in range(0, SAMPLES):
        s = ser.read(1)
        read_data[j][i] = (ord(s))

ser.close()

#%% // Process data
for j in range(0,CHANNELS):
    read_data[j,0:DEADZONE] = read_data[j,DEADZONE+1]   
read_envelope = signal.hilbert(read_data,axis=1)
read_tof = np.argmax(read_envelope,axis=1)



#%%