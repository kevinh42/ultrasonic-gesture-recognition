#%% # Imports and initial setup
import serial
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import time

SAMPLES = 300
CHANNELS = 3
DEADZONE = 15
VOLTAGE_THRESH = 8
STORED_FRAMES = 150
read_data = np.zeros((CHANNELS,SAMPLES))
read_tof = np.zeros(CHANNELS)
stored_tof = np.zeros((CHANNELS,STORED_FRAMES))


#%% # Read data from serial
ser = serial.Serial('COM7', 115200)

while (True):
    ser.write(b'get\n')
    t= time.time()
    
    for j in range(0, CHANNELS):
        s = ser.read(SAMPLES)
        print(s)
            #read_data[j][i] = (ord(s))
    print(time.time()-t)
    #%% # Process data
    read_cleaned = read_data
    for j in range(0,CHANNELS):
        read_cleaned[j,0:DEADZONE] = read_cleaned[j,DEADZONE+1]   
    #read_envelope = signal.hilbert(read_data,axis=1)

    read_cleaned[read_cleaned < VOLTAGE_THRESH] = 0
    # for j in range(0, CHANNELS):
    #     if r < VOLTAGE_THRESH:
    #         r = 0
    read_tof = np.argmax(read_cleaned,axis=1)

    stored_tof = np.roll(stored_tof,-1, axis=1)
    stored_tof[:,-1] = read_tof
    #med_tof

#%%
ser.close()

# %%
