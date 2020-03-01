#ifndef ULTRASONIC_H
#define ULTRASONIC_H

#include <constants.h>

class BinaryMatrix{

    private:
        int time_of_flight[CONSTS::ROWS*CONSTS::COLS] = {0};
    public:
        BinaryMatrix();
        bool matrix[CONSTS::ROWS*CONSTS::COLS][CONSTS::TIME] = {{0}};
        void wipe();

};

#endif