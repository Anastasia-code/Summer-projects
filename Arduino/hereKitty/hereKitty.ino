#include <Servo.h>                           // Include servo library

Servo servoLeft;                             // Declare left servo signal
Servo servoRight;                            // Declare right servo signal

int lWhisker=7;
int rWhisker=5;
//int PIEZOPIN=4;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(lWhisker, INPUT);
  pinMode(rWhisker, INPUT);
//  pinMode(PIEZOPIN, OUTPUT);
  
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12
  servoLeft.writeMicroseconds(1500);        // Calibrate left servo
  servoRight.writeMicroseconds(1500);       // Calibrate right servo
//  noTone(PIEZOPIN);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  servoLeft.writeMicroseconds(1700);        
  servoRight.writeMicroseconds(1500);
  
  int lWhiskerVal=digitalRead(lWhisker);
  Serial.print("Left: ");
  Serial.println(lWhiskerVal);
  int rWhiskerVal=digitalRead(rWhisker);
  Serial.print("Right: ");
  Serial.println(rWhiskerVal);
//  noTone(PIEZOPIN);
 
  if (lWhiskerVal==0 || rWhiskerVal==0){   //if a whisker is touched
    Serial.println("Whiskers are sensed.");
    servoLeft.writeMicroseconds(1300);        //goes backward
    servoRight.writeMicroseconds(1700);
//    delay(2000);

    servoLeft.writeMicroseconds(1300);        //turn left on contact (varies between 90 and 360 deg)
    servoRight.writeMicroseconds(1300);
//    delay(600);

//    tone(PIEZOPIN,400);
//    delay(100);
//    noTone(PIEZOPIN);
    
  } 
  
  delay(1000);
}
