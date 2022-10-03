#include <Ticker.h>

int value_bot_1;
int value_bot_2;
int value_bot_3;
int value_bot_4;

int tiempo = 300;

void get_bot_1()
{
  value_bot_1 = digitalRead(9);
  Serial.println("bot[1]:" + String(value_bot_1));
}
Ticker tic_bot_1(get_bot_1, tiempo);

void get_bot_2()
{
  value_bot_2 = digitalRead(10);
  Serial.println("bot[2]:" + String(value_bot_2));
}
Ticker tic_bot_2(get_bot_2, tiempo);

void get_bot_3()
{
  value_bot_3 = digitalRead(11);
  Serial.println("bot[3]:" + String(value_bot_3));
}
Ticker tic_bot_3(get_bot_3, tiempo);

void get_bot_4()
{
  value_bot_4 = digitalRead(12);
  Serial.println("bot[4]:" + String(value_bot_4));
}
Ticker tic_bot_4(get_bot_4, tiempo);

void setup() {
  Serial.begin(9600);
  
  for(int i = 9; i<=12; i++)
  {
    pinMode(i, INPUT);
  }

  tic_bot_1.start();
  tic_bot_2.start();
  tic_bot_3.start();
  tic_bot_4.start();
}

void loop() {
  tic_bot_1.update();
  tic_bot_2.update();
  tic_bot_3.update();
  tic_bot_4.update();


}
