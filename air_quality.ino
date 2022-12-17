#include "MQ135.h"
#define DIGITALPIN 3    //  Define Analog PIN on Arduino Board
MQ135 gasSensor = MQ135(DIGITALPIN);
void setup()
{ 
  Serial.begin(9600);
  delay(3000);
}

void loop() {
  float ppm = gasSensor.getPPM();
  
  // for printing the rzero calibrate value (initiation phase)
  // float rzero = gasSensor.getRZero();
  //   Serial.println(rzero);

  // for printing the ppm value
  delay(1000);
  Serial.println(ppm);
}