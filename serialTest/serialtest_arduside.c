#include<SoftwareSerial.h>
#include<MECHA_PMS5003ST.h>
#include<avr/sleep.h>
#include<avr/power.h>

SoftwareSerial RPI(2,3);
SoftwareSerial pmsSerial(4,5);
SoftwareSerial dustSerial(6,7);
MECHA_PMS5003ST pms(&pmsSerial);

int pin2 = 2;

void pin2Interrupt(void){
detachInterrupt(0);
}

void enterSleep(void)
{
  attachInterrupt(0, pin2Interrupt, LOW);

  set_sleep_mode(SLEEP_MODE_IDLE);

  sleep_enable();

  /* Now enter sleep mode. */
  sleep_mode();

  /* The program will continue from here after the timer timeout*/
  sleep_disable(); /* First thing to do is disable sleep. */

  /* Re-enable the peripherals. */
  power_all_enable();
}

void setup(){
    RPI.begin(9600);
    pms.begin();
    pms.setMode(PASSIVE);
    pinMode(pin2, INPUT);
}

void loop(){
    if(RPI.available()){
        String req; 
        req = RPI.readStringUntil('\n');
        if(req.equals("update")){
            getData();
        }
        else if(req.equals("sleep")){

            pms.sleep();
            enterSleep();
        }
        else if(req.equals("wakeup")){
            pms.wakeUp();
        }
    }
}


void getData(){
    /*
    pms.request();
    pms.read();
    RPI.print(pms.getTemp()); 
    */
    RPI.println("10");
    RPI.println("20");
    RPI.println("30");
    RPI.println("40");
    RPI.println("50");
}