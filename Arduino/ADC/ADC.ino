#include <Ticker.h>

int value_pot_1;
int value_pot_2;
int value_pot_3;
int value_pot_4;

int pos1;
int pos2;
int pos3;
int pos4;

char input;

void get_pot_1()
{
  value_pot_1 = analogRead(A0);
  Serial.println("pot[1]:" + String(value_pot_1));
}
Ticker tic_pot_1(get_pot_1, 500);

void get_pot_2()
{
  value_pot_2 = analogRead(A1);
  Serial.println("pot[2]:" + String(value_pot_2));
}
Ticker tic_pot_2(get_pot_2, 500);

void get_pot_3()
{
  value_pot_3 = analogRead(A2);
  Serial.println("pot[3]:" + String(value_pot_3));
}
Ticker tic_pot_3(get_pot_3, 500);

void get_pot_4()
{
  value_pot_4 = analogRead(A3);
  Serial.println("pot[4]:" + String(value_pot_4));
}
Ticker tic_pot_4(get_pot_4, 500);

void setup() {
  Serial.begin(9600);

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);

  tic_pot_1.start();
  tic_pot_2.start();
  tic_pot_3.start();
  tic_pot_4.start();

}

void loop() {
  tic_pot_1.update();
  tic_pot_2.update();
  tic_pot_3.update();
  tic_pot_4.update();
}
