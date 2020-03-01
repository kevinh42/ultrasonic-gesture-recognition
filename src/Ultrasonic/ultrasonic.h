#ifndef ULTRASONIC_H
#define ULTRASONIC_H

#include <constants.h>

class BinaryMatrix{
    private:
        int time_of_flight[CONSTS::ROWS*CONSTS::COLS] = {0};
    public:
        BinaryMatrix();
        bool bin_matrix[CONSTS::ROWS*CONSTS::COLS][CONSTS::TIME] = {{0}};
        void reset();
};

class ToFMatrix{
    private:

    public:
        ToFMatrix();
        int tof_matrix[CONSTS::ROWS*CONSTS::COLS] = {CONSTS::TIME};
        void update(int time);
        void reset();
};

#endif