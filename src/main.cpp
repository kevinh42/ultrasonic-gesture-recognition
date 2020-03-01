#include <Arduino.h>
#include <constants.h>
#include <Ultrasonic/ultrasonic.h>

BinaryMatrix* bin_mat;

void setup() {
  Serial.begin(9600);
  bin_mat = new BinaryMatrix();
}

void loop() {
  Serial.println(bin_mat->matrix[0][0]);
  bin_mat->matrix[0][0] = 1;
  delay(1000);
  Serial.println(bin_mat->matrix[0][0]);
  bin_mat->wipe();
  delay(1000);
}