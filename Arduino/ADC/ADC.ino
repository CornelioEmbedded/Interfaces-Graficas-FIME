
int value_pot_1;
int pos;

void setup() {
  Serial.begin(9600);

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);

}

void loop() {

  value_pot_1 = analogRead(A0);
  pos = map(value_pot_1, 0, 1023, 0, 100);

  Serial.println(value_pot_1);

}
