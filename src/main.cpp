#include <Arduino.h>
#include <Metro.h>

#include <constants.h>
#include <Ultrasonic/ultrasonic.h>

ToFMatrix* tof;
//Metro echo_metro(CONSTS::METRO_TIME);
//uint8_t echo_timer = 0;
uint8_t read_data[CONSTS::ROWS*CONSTS::COLS][CONSTS::SAMPLES]={0};

void setup() {
  Serial.begin(9600);
  pinMode(PINS::sync_pin, INPUT);
  for (uint8_t j = 0; j < sizeof(PINS::pins)/sizeof(PINS::pins[0]); j++){
    pinMode(PINS::pins[j], INPUT);
  }
  analogReadRes(8);
  analogReadAveraging(1);
  /*
  tof = new ToFMatrix();
  for (int i = 0; i<CONSTS::ROWS*CONSTS::COLS; i++){
    pinMode(PINS::pins[i], INPUT);
  }
  */
}

void loop() {
  for (int j = 0; j < CONSTS::ROWS*CONSTS::COLS; j++){
    /*
    while(!digitalRead(PINS::sync_pin)){
      //wait until sync pulse
    }
    */
    for (int i = 0; i < CONSTS::SAMPLES; i++){
      read_data[j][i] = analogRead(PINS::pins[j]);
    }
  }
  
  if (Serial.available()){
    String get = Serial.readStringUntil('\n');
    if (get=="get"){
      for (int j = 0; j < CONSTS::ROWS*CONSTS::COLS; j++){
        Serial.write(read_data[j],CONSTS::SAMPLES);
      }
    }

  }

  /*
  while (echo_timer<CONSTS::MAX_PERIODS){
    if (echo_metro.check()){
      echo_timer++;
      if (echo_timer > CONSTS::DEADZONE_THRESH){
        tof->update(echo_timer);
      }
    }
  }
  
  tof->send();
  tof->reset();
  echo_timer = 0;
  echo_metro.reset();
  */
}