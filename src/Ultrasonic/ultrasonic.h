#ifndef ULTRASONIC_H
#define ULTRASONIC_H

#include <Config/constants.h>
#include <Arduino.h>

class ToFMatrix{
    private:
        
    public:
        uint8_t tof_matrix[CONSTS::FRAMES][CONSTS::ROWS*CONSTS::COLS] = {{CONSTS::MAX_PERIODS}};
        ToFMatrix();
        void update(uint8_t frame, uint8_t time);
        void reset();
        void send();
};

/*
class ThreeDArray{
    private:
        int vals[dim0*dim1*dim2];
    public:
        ThreeDArray(int dim0, int dim1, int dim2);
        int dim0;
        int dim1;
        int dim2;
        void clear();
        void place(int val, int ind0, int ind1, int ind2);
        int get(int ind0, int ind1, int ind2);
        void send();
        

};
*/
#endif