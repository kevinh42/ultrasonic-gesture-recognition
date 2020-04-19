#%% # Imports
import serial
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from gui import GUI
from scipy import ndimage
from scipy import fftpack
from tkinter import *
import time
import configparser

config = configparser.ConfigParser()
config.read("src/config/config.ini")
default = config["DEFAULT"]
if bool(default["DEMO"]):
    TRANSDUCER_ORDER = [1,2,0] # left to right
    SAMPLES = 300
    DEADZONE = 40
COM_PORT = default["COM_PORT"]
CHANNELS = int(default["CHANNELS"])
FRAMES = int(default["FRAMES"])
VOLTAGE_THRESH = int(default["VOLTAGE_THRESH"])
TOF_THRESH = int(default["TOF_THRESH"])
STORED_FRAMES = int(default["STORED_FRAMES"])
MEDFILT_KERNEL = int(default["MEDFILT_KERNEL"])
STD_THRESH = int(default["STD_THRESH"])


# functions
def demo_tap_or_swipe(tofs): #distinguishes between tap and swipe gestures
    abovethresh = tofs[tofs>TOF_THRESH]
    #print(np.std(abovethresh))
    return np.std(abovethresh)<STD_THRESH
    #returns 1 if swipe, 0 if tap

def demo_classify(tofs, gui): #classify gesture
    chs = tofs.shape[0]
    channel_start_index = np.zeros(chs)
    channel_end_index = np.zeros(chs)
    votes = 0
    for i in range(0,chs):
        channel_start_index[i] = np.argmax(tofs[i]>0)
        channel_end_index[i] = tofs.shape[1] - np.argmax(np.flip(tofs[i])>0)
        votes += demo_tap_or_swipe(tofs[i])
    plt.legend()
    gesture = ""
    if votes >=2: #swipe
        gesture = "Swipe"
        xdirection = 0
        ydirection = 0
        if (channel_start_index[TRANSDUCER_ORDER[2]]>channel_start_index[TRANSDUCER_ORDER[0]]):
            xdirection +=2
        else:
            xdirection -=2
        if (channel_end_index[TRANSDUCER_ORDER[2]]>channel_end_index[TRANSDUCER_ORDER[0]]):
            xdirection +=2
        else:
            xdirection -=2

        if xdirection>0:
            gesture += "-Right"
        elif xdirection<0:
            gesture += "-Left"
    else: #tap
        gesture = "Tap"
    gui.update(tofs, gesture)

def features(tofs):
    feats = {}
    stds = np.zeros(CHANNELS)
    for i in CHANNELS:
        std[i] = np.std(tofs[i][tofs[i]>TOF_THRESH])
    feats["Std"] = stds
    # More features can be added as needed
    return feats

def classify(feats):
    # Machine learning can be implemented here
    stds = feats["Std"]
    if mean(stds) > STD_THRESH:
        gesture = "Tap"
    else: 
        gesture = "Swipe"
    return gesture

if bool(default["DEMO"]):
    #For use with demonstration unit
    #analog_sample_mode
    #%% # setup
    read_data = np.zeros((FRAMES,CHANNELS,SAMPLES))
    read_tof = np.zeros((FRAMES,CHANNELS))
    stored_tof = np.zeros((CHANNELS,STORED_FRAMES))

    GESTURE_BEGAN = 0
    gesture_start_index = 0

    # Read data from serial
    ser = serial.Serial(COM_PORT, 115200)
    window = Tk()
    gui = GUI(window)
    while (True):
        #t= time.time()
        window.update_idletasks()
        window.update()
        ser.write(b'get\n')
        s = ser.read(FRAMES*CHANNELS*SAMPLES)
        #print(time.time()-t)
        read_data = np.array([a for a in s]).reshape((FRAMES,CHANNELS,SAMPLES))
        
        # Process data
        read_cleaned = read_data
        for k in range(0,FRAMES):
            for j in range(0,CHANNELS):
                read_cleaned[k,j,0:DEADZONE] = read_cleaned[k,j,DEADZONE+1]   
        
        read_cleaned[read_cleaned < VOLTAGE_THRESH] = 0
        read_tof = np.argmax(read_cleaned,axis=2)
        
        stored_tof = np.roll(stored_tof,-FRAMES, axis=1)
        stored_tof[:,-FRAMES:] = read_tof.transpose()
        
        med_tof = ndimage.median_filter(stored_tof,(1,MEDFILT_KERNEL))
        #Gesture started?
        if GESTURE_BEGAN:
            #Gesture ended?
            a = med_tof[:,-FRAMES:]
            gesture_start_index -= FRAMES
            if a[a>0].size < FRAMES/3:
                #classify gesture
                demo_classify(med_tof[:,gesture_start_index:], gui)
                #reset flags
                GESTURE_BEGAN = 0
        else:
            a = med_tof[:,-FRAMES:]
            if a[a>0].size > FRAMES/3:
                GESTURE_BEGAN = 1
                gesture_start_index = STORED_FRAMES - FRAMES
    ser.close()
else:
    #digital_tof_mode
    read_tof = np.zeros((FRAMES,CHANNELS))
    stored_tof = np.zeros((CHANNELS,STORED_FRAMES))

    GESTURE_BEGAN = 0
    gesture_start_index = 0

    # Read data from serial
    ser = serial.Serial(COM_PORT, 115200)
    window = Tk()
    gui = GUI(window)
    while (True):
        #t= time.time()
        window.update_idletasks()
        window.update()
        ser.write(b'get\n')
        s = ser.read(FRAMES*CHANNELS)
        #print(time.time()-t)
        read_tof = np.array([a for a in s]).reshape((FRAMES,CHANNELS))

        stored_tof = np.roll(stored_tof,-FRAMES, axis=1)
        stored_tof[:,-FRAMES:] = read_tof.transpose()
        
        med_tof = ndimage.median_filter(stored_tof,(1,MEDFILT_KERNEL))
        #Gesture started?
        if GESTURE_BEGAN:
            #Gesture ended?
            a = med_tof[:,-FRAMES:]
            gesture_start_index -= FRAMES
            if a[a>0].size < FRAMES/3:
                #extract features
                feats = features(med_tof)
                #classify with features
                gesture = classify(feats)
                gui.update(tofs,gesture)
                #reset flags
                GESTURE_BEGAN = 0
        else:
            a = med_tof[:,-FRAMES:]
            if a[a>0].size > FRAMES/3:
                GESTURE_BEGAN = 1
                gesture_start_index = STORED_FRAMES - FRAMES
    ser.close()