#%% # Imports and initial setup
import serial
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy import ndimage
from scipy import fftpack
import time

SAMPLES = 300
CHANNELS = 3
FRAMES = 10
DEADZONE = 25
VOLTAGE_THRESH = 15
TOF_THRESH = 0
STORED_FRAMES = 1500
MEDFILT_KERNEL = 11
read_data = np.zeros((FRAMES,CHANNELS,SAMPLES))
read_tof = np.zeros((FRAMES,CHANNELS))
stored_tof = np.zeros((CHANNELS,STORED_FRAMES))

GESTURE_BEGAN = np.zeros()
GESTURE_START_INDICES = np.zeros()
GESTURE_ENDED = 0


#%% # Read data from serial
ser = serial.Serial('COM7', 115200)

while (True):
    t= time.time()
    #
    ser.write(b'get\n')
    s = ser.read(FRAMES*CHANNELS*SAMPLES)
    print(time.time()-t)
    read_data = np.array([a for a in s]).reshape((FRAMES,CHANNELS,SAMPLES))
    
    # Process data
    
    read_cleaned = read_data
    for k in range(0,FRAMES):
        for j in range(0,CHANNELS):
            read_cleaned[k,j,0:DEADZONE] = read_cleaned[k,j,DEADZONE+1]   
    #read_envelope = signal.hilbert(read_data,axis=1)
    
    read_cleaned[read_cleaned < VOLTAGE_THRESH] = 0
    # for j in range(0, CHANNELS):
    #     if r < VOLTAGE_THRESH:
    #         r = 0
    read_tof = np.argmax(read_cleaned,axis=2)
    
    stored_tof = np.roll(stored_tof,-FRAMES, axis=1)
    stored_tof[:,-FRAMES:] = read_tof.transpose()
    
    med_tof = ndimage.median_filter(stored_tof,(1,MEDFILT_KERNEL))
    #Gesture started?
    if np.sum(GESTURED_BEGAN):
    #    if med_tof[]
        #Gesture ended?
    else:


    
    fft_tof = fftpack.fft(med_tof, axis=1)
    grad = np.gradient(med_tof, axis=1)
    

    #med_tof

#%%
ser.close()

#%%
# Detect gesture
