#include <Ultrasonic/ultrasonic.h>

BinaryMatrix::BinaryMatrix(){
}

void BinaryMatrix::reset(){
    //clear matrix
    for (int i = 0; i<CONSTS::ROWS*CONSTS::COLS; i++){
        for (int j = 0; j<CONSTS::TIME; j++){
            bin_matrix[i][j]=0;
        }
    }
}

ToFMatrix::ToFMatrix(){
}

void ToFMatrix::reset(){
    //clear matrix
    for (int i = 0; i<CONSTS::ROWS*CONSTS::COLS; i++){
            tof_matrix[i]=CONSTS::TIME;
    }
}

void ToFMatrix::update(int time){
    //TODO: update only if corresponding pin is HIGH
    for (int i = 0; i<CONSTS::ROWS*CONSTS::COLS; i++){
        if (tof_matrix[i]>time){
            tof_matrix[i] = time;
        }
    }
}