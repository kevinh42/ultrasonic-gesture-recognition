#include <Ultrasonic/ultrasonic.h>

BinaryMatrix::BinaryMatrix(){

}

void BinaryMatrix::wipe(){
    //clear matrix
    for (int i = 0; i<CONSTS::ROWS*CONSTS::COLS; i++){
        for (int j = 0; j<CONSTS::TIME; j++){
            matrix[i][j]=0;
        }
    }
}