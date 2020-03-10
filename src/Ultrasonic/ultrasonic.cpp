#include <Ultrasonic/ultrasonic.h>
#include <Arduino.h>

BinaryMatrix::BinaryMatrix(){
}

void BinaryMatrix::reset(){
    //clear matrix
    for (uint8_t i = 0; i<CONSTS::ROWS*CONSTS::COLS; i++){
        for (uint8_t j = 0; j<CONSTS::MAX_PERIODS; j++){
            bin_matrix[i][j]=0;
        }
    }
}

ToFMatrix::ToFMatrix(){
}

void ToFMatrix::reset(){
    //clear matrix
    for (uint8_t i = 0; i<CONSTS::ROWS*CONSTS::COLS; i++){
            tof_matrix[i]=CONSTS::MAX_PERIODS;
            peak_matrix[i]=0;
    }
}

void ToFMatrix::update(uint8_t time){
    for (uint8_t i = 0; i<CONSTS::ROWS*CONSTS::COLS; i++){
        uint8_t read = analogRead(PINS::pins[i]);
        if (read>peak_matrix[i]){
            peak_matrix[i] = read;
            tof_matrix[i] = time;
        }
    }
}

void ToFMatrix::send(){
    Serial.write(tof_matrix,CONSTS::ROWS*CONSTS::COLS);
} 