#ifndef ULTRASONIC_H
#define ULTRASONIC_H

#include <constants.h>
#include <Arduino.h>

class BinaryMatrix{
    private:
        uint8_t tof_matrix[CONSTS::ROWS*CONSTS::COLS] = {0};
    public:
        BinaryMatrix();
        bool bin_matrix[CONSTS::ROWS*CONSTS::COLS][CONSTS::MAX_PERIODS] = {{0}};
        void reset();
};

class ToFMatrix{
    private:
        uint8_t tof_matrix[CONSTS::ROWS*CONSTS::COLS] = {CONSTS::MAX_PERIODS};
        uint8_t peak_matrix[CONSTS::ROWS*CONSTS::COLS] = {0};
    public:
        ToFMatrix();
        void update(uint8_t time);
        void reset();
        void send();
};

#endif