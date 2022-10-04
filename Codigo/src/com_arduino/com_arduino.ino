#include <Ticker.h>

int value_pot_1;
int value_pot_2;
int value_pot_3;
int value_pot_4;

int value_bot_1;
int value_bot_2;
int value_bot_3;
int value_bot_4;

int tiempo = 200;
int tiempo1 = 200;

char input;
char input_2;

/************************FUNCIONES DE POTENCIOMETROS*************************************/

void get_pot_1()
{
  value_pot_1 = analogRead(A0);
  Serial.println("pot[1]:" + String(value_pot_1));
}
Ticker tic_pot_1(get_pot_1, tiempo);

void get_pot_2()
{
  value_pot_2 = analogRead(A1);
  Serial.println("pot[2]:" + String(value_pot_2));
}
Ticker tic_pot_2(get_pot_2, tiempo);

void get_pot_3()
{
  value_pot_3 = analogRead(A2);
  Serial.println("pot[3]:" + String(value_pot_3));
}
Ticker tic_pot_3(get_pot_3, tiempo);

void get_pot_4()
{
  value_pot_4 = analogRead(A3);
  Serial.println("pot[4]:" + String(value_pot_4));
}
Ticker tic_pot_4(get_pot_4, tiempo1);

/************************FUNCIONES DE BOTONES*************************************/

void get_bot_1()
{
  value_bot_1 = digitalRead(9);
  Serial.println("bot[1]-" + String(value_bot_1));
}
Ticker tic_bot_1(get_bot_1, tiempo1);

void get_bot_2()
{
  value_bot_2 = digitalRead(10);
  Serial.println("bot[2]-" + String(value_bot_2));
}
Ticker tic_bot_2(get_bot_2, tiempo1);

void get_bot_3()
{
  value_bot_3 = digitalRead(11);
  Serial.println("bot[3]-" + String(value_bot_3));
}
Ticker tic_bot_3(get_bot_3, tiempo1);

void get_bot_4()
{
  value_bot_4 = digitalRead(12);
  Serial.println("bot[4]-" + String(value_bot_4));
}
Ticker tic_bot_4(get_bot_4, tiempo1);


void setup() {
  Serial.begin(9600);

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);

  for(int i = 2; i<=8; i++)
  {
    pinMode(i,OUTPUT);
  }

  for(int i = 9; i<=12; i++)
  {
    pinMode(i, INPUT);
  }

  tic_pot_1.start();
  tic_pot_2.start();
  tic_pot_3.start();
  tic_pot_4.start();

  tic_bot_1.start();
  tic_bot_2.start();
  tic_bot_3.start();
  tic_bot_4.start();

}

void loop(){




  tic_pot_1.update();
  tic_pot_2.update();
  tic_pot_3.update();
  tic_pot_4.update();

  if(Serial.available() > 0)
  {
    input = Serial.read();
    display_decision(input);
    
  }
}

/************************FUNCIONES DEL DISPLAY*************************************/

void displayLed(int numero)
{
  switch(numero)
  {
    case 0:
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(4,HIGH);
    digitalWrite(6,HIGH);
    digitalWrite(5,HIGH);
    digitalWrite(7,HIGH);
    digitalWrite(8,LOW);
    break;
    
    case 1:
    digitalWrite(2,HIGH);
    digitalWrite(3,LOW);
    digitalWrite(4,LOW);
    digitalWrite(6,LOW);
    digitalWrite(5,HIGH);
    digitalWrite(7,LOW);
    digitalWrite(8,LOW);
    break;

    case 2:
    digitalWrite(2,LOW);
    digitalWrite(3,HIGH);
    digitalWrite(4,HIGH);
    digitalWrite(6,HIGH);
    digitalWrite(5,HIGH);
    digitalWrite(7,LOW);
    digitalWrite(8,HIGH);
    break;
    

    case 3: //2,3,5,6,8
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(4,LOW);
    digitalWrite(6,HIGH);
    digitalWrite(5,HIGH);
    digitalWrite(7,LOW);
    digitalWrite(8,HIGH);
    break;

    case 4: //2,3,5,6,8
    digitalWrite(2,HIGH);
    digitalWrite(3,LOW);
    digitalWrite(4,LOW);
    digitalWrite(6,LOW);
    digitalWrite(5,HIGH);
    digitalWrite(7,HIGH);
    digitalWrite(8,HIGH);
    break;

    case 5: 
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(4,LOW);
    digitalWrite(6,HIGH);
    digitalWrite(5,LOW);
    digitalWrite(7,HIGH);
    digitalWrite(8,HIGH);
    break;

    case 6:
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(4,HIGH);
    digitalWrite(6,HIGH);
    digitalWrite(5,LOW);
    digitalWrite(7,HIGH);
    digitalWrite(8,HIGH);
    break;

    case 7: //2,3,5,6,8
    digitalWrite(2,HIGH);
    digitalWrite(3,LOW);
    digitalWrite(4,LOW);
    digitalWrite(6,HIGH);
    digitalWrite(5,HIGH);
    digitalWrite(7,LOW);
    digitalWrite(8,LOW);
    break;

    case 8: 
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(4,HIGH);
    digitalWrite(6,HIGH);
    digitalWrite(5,HIGH);
    digitalWrite(7,HIGH);
    digitalWrite(8,HIGH);
    break;

    case 9: //2,3,5,6,8
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(4,LOW);
    digitalWrite(6,HIGH);
    digitalWrite(5,HIGH);
    digitalWrite(7,HIGH);
    digitalWrite(8,HIGH);
    break;

    case 10:
    digitalWrite(2,LOW);
    digitalWrite(3,LOW);
    digitalWrite(4,LOW);
    digitalWrite(6,LOW);
    digitalWrite(5,LOW);
    digitalWrite(7,LOW);
    digitalWrite(8,LOW);
    break;
    

    
  }
  
}

void display_decision(int input)
{
  switch(input)
    { 
      case '0':
      displayLed(0);
      break;
      
      case '1':
      displayLed(1);
      break;
      
      case '2':
      displayLed(2);
      break;

      case '3':
      displayLed(3);
      break;

      case '4':
      displayLed(4);
      break;

      case '5':
      displayLed(5);
      break;

      case '6':
      displayLed(6);
      break;

      case '7':
      displayLed(7);
      break;

      case '8':
      displayLed(8);
      break;

      case '9':
      displayLed(9);
      break;

      default:
      displayLed(10);
      break;
    }
}
