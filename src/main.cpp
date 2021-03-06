#include <Arduino.h>
#include <Metro.h>

#include <Config/constants.h>
#include <Ultrasonic/ultrasonic.h>

ToFMatrix* tof;
Metro echo_metro(CONSTS::METRO_TIME);
uint8_t echo_timer = 0;
uint8_t send_tof[CONSTS::FRAMES*CONSTS::ROWS*CONSTS::COLS] = {0};
uint8_t read_data[CONSTS::FRAMES][CONSTS::ROWS*CONSTS::COLS][CONSTS::SAMPLES]={0};
uint8_t send_data[CONSTS::FRAMES*CONSTS::ROWS*CONSTS::COLS*CONSTS::SAMPLES] = {0};

void setup() {
  Serial.begin(115200);
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

  auto analog_sample_mode = [=](){
    for (int k = 0; k < CONSTS::FRAMES; k++){
      for (int j = 0; j < CONSTS::ROWS*CONSTS::COLS; j++){
        while(!digitalReadFast(PINS::sync_pin)){
          //wait until sync pulse
        }
        
        for (int i = 0; i < CONSTS::SAMPLES; i++){
          read_data[k][j][i] = analogRead(PINS::pins[j]);
        }
      }
    }
    if (Serial.available()){
      String get = Serial.readStringUntil('\n');
      if (get=="get"){
        for (int k = 0; k < CONSTS::FRAMES; k++){
          for (int j = 0; j < CONSTS::ROWS*CONSTS::COLS; j++){
            for (int i = 0; i < CONSTS::SAMPLES; i++){
              send_data[k*CONSTS::ROWS*CONSTS::COLS*CONSTS::SAMPLES+j*CONSTS::SAMPLES+i] = read_data[k][j][i];
            }
          }
        }
        Serial.write(send_data,CONSTS::FRAMES*CONSTS::ROWS*CONSTS::COLS*CONSTS::SAMPLES);
      }
    }
  };
  auto digital_tof_mode = [=](){
    for (uint8_t k = 0; k<CONSTS::FRAMES; k++){
      while(!digitalReadFast(PINS::sync_pin)){
          //wait until sync pulse
      }
      echo_timer = 0;
      echo_metro.reset();
      while (echo_timer<CONSTS::MAX_PERIODS){
        if (echo_metro.check()){
          echo_timer++;
          if (echo_timer > CONSTS::DEADZONE_THRESH){
            tof->update(k,echo_timer);
          }
        }
      }
    }
    if (Serial.available()){
      String get = Serial.readStringUntil('\n');
      if (get=="get"){
        for (int k = 0; k < CONSTS::FRAMES; k++){
          for (int j = 0; j < CONSTS::ROWS*CONSTS::COLS; j++){
            send_tof[k*CONSTS::ROWS*CONSTS::COLS*CONSTS::SAMPLES+j] = tof->tof_matrix[k][j];
          }
        }
        Serial.write(send_tof,CONSTS::FRAMES*CONSTS::ROWS*CONSTS::COLS*CONSTS::SAMPLES);
      }
    }
    tof->reset();
    };

  if (MODE::DEMO){
    analog_sample_mode();
  } else {
    digital_tof_mode();
  }
  
}