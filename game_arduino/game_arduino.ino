#define joyx1 A0
#define joyy1 A1
#define joyx2 A2
#define joyy2 A3
#define but1 1
#define but2 2

void setup(){
  Serial.begin(9600);
  pinMode(but1,INPUT);
  pinMode(but2,INPUT);
}

void loop(){
  if(Serial.available()>0){
    char c = Serial.read();
    switch(c){
      case 'p':
      Serial.print(analogRead(joyx1));Serial.print(",");
      Serial.print(analogRead(joyy1));Serial.print(",");
      Serial.print(analogRead(joyx2));Serial.print(",");
      Serial.print(analogRead(joyy2));Serial.print(",");
      Serial.print(digitalRead(but1));Serial.print(",");
      Serial.print(digitalRead(but2));Serial.println();
      break;
    }
  }
}
