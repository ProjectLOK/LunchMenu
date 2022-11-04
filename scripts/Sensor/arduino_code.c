#include<SoftwareSerial.h>
#include<MECHA_PMS5003ST.h>
#include<MHZ19.h>
#include<avr/sleep.h>
#include<avr/power.h>

SoftwareSerial pmsSerial(3,4);
SoftwareSerial co2Serial(5,6);
MECHA_PMS5003ST pms(&pmsSerial);
MHZ19 mhz;

int pin2 = 2;


void setup(){
    Serial.begin(115200);
    co2Serial.begin(9600);
    mhz.begin(co2Serial);
    mhz.autoCalibration();
    pms.begin();
    pms.setMode(PASSIVE);
    pinMode(pin2, INPUT);

}


void loop(){
    if(Serial.available()){
        String req; 
        req = Serial.readStringUntil('\n');
        if(req.equals("update")){
            getData();
        }

        else if(req.equals("sleep")){
            pms.sleep();
            Going_To_Sleep();
        }
    }
}


void getData(){
    pms.request();
    pms.read();
    Serial.println(pms.getTemp());
    Serial.println(pms.getHumi());
    Serial.println(pms.getPmAto(10));
    Serial.println(pms.getPmAto(2.5));
    Serial.println(mhz.getCO2());
    Serial.println(pms.getForm());
}


void Going_To_Sleep(){
    sleep_enable();                        // Enabling sleep mode
    attachInterrupt(digitalPinToInterrupt(pin2), wakeUp, RISING);       // attaching a interrupt to pin d2
    set_sleep_mode(SLEEP_MODE_PWR_DOWN);   // Setting the sleep mode, in our case full sleep
    digitalWrite(LED_BUILTIN,LOW);         // turning LED off
   // Serial.println("going to sleep");
    delay(1000);                           // wait a second to allow the led to be turned off before going to sleep
    sleep_mode();                           // activating sleep mode
    //Serial.println("just woke up!");       // next line of code executed after the interrupt
   // digitalWrite(LED_BUILTIN,HIGH);        // turning LED on
  }


void wakeUp(){
    //Serial.println("Interrupt Fired");    // Print message to serial monitor
    sleep_disable();                       // Disable sleep mode
    detachInterrupt(digitalPinToInterrupt(pin2)); // Removes the interrupt from pin 2;
    EIFR |= ( 1 << INTF0 );
    //Serial.print("EIFR: ");
    //Serial.println(EIFR);
    pms.wakeUp();
}
