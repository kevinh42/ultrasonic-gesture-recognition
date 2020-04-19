#include <Ultrasonic/ultrasonic.h>
#include <Arduino.h>

ToFMatrix::ToFMatrix(){
}

void ToFMatrix::reset(){
    //clear matrix
    for (uint8_t k = 0; k<CONSTS::FRAMES; k++){
        for (uint8_t i = 0; i<CONSTS::ROWS*CONSTS::COLS; i++){
                tof_matrix[k][i]=CONSTS::MAX_PERIODS;
        }
    }
}

void ToFMatrix::update(uint8_t frame, uint8_t time){
    for (uint8_t i = 0; i<CONSTS::ROWS*CONSTS::COLS; i++){
        uint8_t read = digitalRead(PINS::pins[i]);
        if (read && time<tof_matrix[frame][i]){
            tof_matrix[frame][i] = time;
        }
    }
}