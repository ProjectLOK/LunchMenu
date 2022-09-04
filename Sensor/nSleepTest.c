#include <avr/sleep.h>   // this AVR library contains the methods that controls the sleep modes
//#define interruptPin 2   // Pin we are going to use to wake up the Arduino

int pin2 = 2;
void setup() {
    Serial.begin(115200);                     // Start Serial Comunication
    pinMode(LED_BUILTIN, OUTPUT);             // We use the led on pin 13 to indecate when Arduino is A sleep
    pinMode(pin2, INPUT);      // Set pin d2 to input using the buildin pullup resistor
    digitalWrite(LED_BUILTIN, HIGH);          // turning LED on
}


void loop() {
   //EIFR |= ( 1 << INTF0 );
   char ib = Serial.read();
   if(ib == '1'){
    Serial.println("I'm awake!");
   }
   else if(ib == '0'){
       // wait 5 seconds before going to sleep
       Going_To_Sleep();
   }
}

void Going_To_Sleep(){

    sleep_enable();                        // Enabling sleep mode
    attachInterrupt(digitalPinToInterrupt(pin2), wakeUp, RISING);       // attaching a interrupt to pin d2
    set_sleep_mode(SLEEP_MODE_PWR_DOWN);   // Setting the sleep mode, in our case full sleep
    digitalWrite(LED_BUILTIN,LOW);         // turning LED off
    Serial.println("going to sleep");
    delay(1000);                           // wait a second to allow the led to be turned off before going to sleep
    sleep_mode();                           // activating sleep mode
    Serial.println("just woke up!");       // next line of code executed after the interrupt 
    digitalWrite(LED_BUILTIN,HIGH);        // turning LED on
  }


void wakeUp(){
    Serial.println("Interrupt Fired");    // Print message to serial monitor
    sleep_disable();                       // Disable sleep mode
    detachInterrupt(digitalPinToInterrupt(pin2)); // Removes the interrupt from pin 2;
    EIFR |= ( 1 << INTF0 );
    Serial.print("EIFR: ");
    Serial.println(EIFR);
}