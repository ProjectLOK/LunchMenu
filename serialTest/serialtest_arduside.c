#include<SoftwareSerial.h>
#include<MECHA_PMS5003ST.h>

SoftwareSerial RPI(2,3);
SoftwareSerial pmsSerial(4,5);
SoftwareSerial dustSerial(6,7);
MECHA_PMS5003ST pms(&pmsSerial);

void setup(){
    RPI.begin(9600);
    pms.begin();
    pms.setMode(PASSIVE);
}

void loop(){
    if(RPI.available()){
        String req; 
        req = RPI.readStringUntil('\n');
        if(req.equals("update")){
            getData();
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