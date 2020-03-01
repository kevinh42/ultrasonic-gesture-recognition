#include <Arduino.h>
#include <Metro.h>

#include <constants.h>
#include <Ultrasonic/ultrasonic.h>

ToFMatrix* tof;
Metro echo_metro(1000);
int echo_timer = 0;

void setup() {
  Serial.begin(9600);
  tof = new ToFMatrix();
}

void loop() {
  while (echo_timer<CONSTS::TIME){
    if (echo_metro.check()){
      echo_timer++;
      tof->update(echo_timer);
    }
  }
  tof->reset();
  echo_timer = 0;
  echo_metro.reset();
}