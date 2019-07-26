int aDigitalPin=13;

void setup() {
  // put your setup code here, to run once:
 pinMode(aDigitalPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int aValue=digitalRead(aDigitalPin);
}
