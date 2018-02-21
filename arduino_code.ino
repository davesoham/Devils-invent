#include <LiquidCrystal.h>
 #define trigPin 13
 #define echoPin 8
 // initialize the library with the numbers of the interface pins
 LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
 int counter = 0;
 int currentState = 0;
 int previousState = 0;
 
 void setup() {
 pinMode(trigPin, OUTPUT);
 pinMode(echoPin, INPUT);
 lcd.begin(16, 2);
 lcd.setCursor(4, 0);
 lcd.print("counter");
 }
 
 void loop() {
 long duration, distance;
 digitalWrite(trigPin, LOW); 
 delayMicroseconds(100);  /*Determine bug speed and change*/
 digitalWrite(trigPin, HIGH);
 delayMicroseconds(2000); /*Determine bug speed and change*/
 digitalWrite(trigPin, LOW);
 duration = pulseIn(echoPin, HIGH);
 distance = (duration/2) / 29.1;
 if (distance <= 3.5){ - Can be changed
 currentState = 1;
 }
 else {
 currentState = 0;
 }
 delay(1000);  /*Determine bug speed and change*/
 if(currentState != previousState){
 if(currentState == 1){
 counter = counter + 1;
 lcd.setCursor(4,1);
 lcd.print(counter);
 }
 }
 }


