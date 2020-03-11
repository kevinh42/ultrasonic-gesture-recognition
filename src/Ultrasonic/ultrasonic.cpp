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

/*
ThreeDArray::ThreeDArray(int dim0, int dim1, int dim2){
    this->dim0 = dim0;
    this->dim1 = dim1;
    this->dim2 = dim2;
}

void ThreeDArray::clear(){
    this->vals = {0};
}

void ThreeDArray::place(int val, int ind0, int ind1, int ind2){
    //TODO
}

int ThreeDArray::get(int ind0, int ind1, int ind2){

}

void ThreeDArray::send(){

}
*/