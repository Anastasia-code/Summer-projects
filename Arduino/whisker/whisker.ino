int lWhisker=7;
int rWhisker=5;
//int PIEZOPIN=4;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(lWhisker, INPUT);
  pinMode(rWhisker, INPUT);
//  pinMode(PIEZOPIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int lWhiskerVal=digitalRead(lWhisker);
  Serial.print("Left: ");
  Serial.println(lWhiskerVal);
  int rWhiskerVal=digitalRead(rWhisker);
  Serial.print("Right: ");
  Serial.println(rWhiskerVal);

//  tone(PIEZOPIN,500);
//  delay(100);
//  noTone(PIEZOPIN);
//  delay(100);
 
  if (lWhiskerVal==0){   
    Serial.println("Left Whisker is sensed.");
  } if (rWhiskerVal==0){
    Serial.println("Right Whisker is sensed.");  
  }
  delay(1000);
}
