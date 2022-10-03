int Button;

void setup() {
  Serial.begin(9600);
  pinMode(9, INPUT);
}

void loop() {

  Button = digitalRead(9);
  Serial.println(Button);
  delay(100);


}
