**Software Pipeline for Ultrasonic Gesture Recognition**

Designed as part of ENPH 459 Capstone course

Our data pipeline consists of two components:
1. Data acquisition using Teensy 4.0 microcontroller (C++/PlatformIO)
2. Gesture recognition on the device to be controlled (Python)

Requirements:
- VSCode with PlatformIO extension
- Python 3.7 64-bit

How to use with demonstration unit:
1. Connect the demonstration unit by USB to the PC.
2. In VSCode, upload the microcontroller code using PlatformIO (this step is not required after first upload.)
2. Check the COM port the microcontroller is using and modify "demo_config.ini" if necessary.
3. Run "process.py" on the PC.

For future use:

The demonstration unit uses modified code in some instances since it uses analog sampling instead of a digital thresholding method. Comments in the code indicate where this occurs. As a simple procedure, modify "constants.h" and "config.ini" when using different hardware.

The "features" and "classify" functions are the sections that should be expanded when implementing machine learning.