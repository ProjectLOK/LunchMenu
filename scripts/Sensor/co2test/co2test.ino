#include<SoftwareSerial.h>
#include<MHZ19.h>
SoftwareSerial co2Serial(5,6);
MHZ19 mhz;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  co2Serial.begin(9600);
  mhz.begin(co2Serial);
  mhz.autoCalibration();

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(mhz.getCO2());
  delay(1000);

}
