#ifndef CONSTANTS_H
#define CONSTANTS_H

#include <Arduino.h>

namespace MODE {
    const int DEMO = true; // Turn this on when using demonstration unit
}

namespace CONSTS {
    const int ROWS = 1;
    const int COLS = 3;
    const uint8_t MAX_PERIODS = 255; //Max periods for ToF
    const int SAMPLES = 300; //Samples for analog reading
    const int METRO_TIME = 50; //Duration of an interval for metronome
    const int DEADZONE_THRESH = 0; //Timer threshold for deadzone
    const int FRAMES = 10; //Frames to keep before sending
}

namespace PINS {
    const int pins[CONSTS::ROWS*CONSTS::COLS] = {A0,A1,A2};
    const int sync_pin = 17;
}

#endif