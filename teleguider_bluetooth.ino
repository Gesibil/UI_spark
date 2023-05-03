// Prérequis savoir utiliser un timer 
#include <HC05.h> // pour le bluetooth

// Encoder output to Arduino Interrupt pin. Tracks the tick count.
#define ENC_IN_LEFT_A 2
#define ENC_IN_RIGHT_A 3
// Other encoder output to Arduino to keep track of wheel direction
// Tracks the direction of rotation.
#define ENC_IN_LEFT_B 4
#define ENC_IN_RIGHT_B 11

char t;

// Motor A connections
const int enA = 9;// right
const int in1 = 5;
const int in2 = 6;
// Motor B connections
const int enB = 10; //right
const int in3 = 7;
const int in4 = 8;
const int val0,val1,val2,val3 ;



void setup() {
  // Motor control pins are outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  
  // Turn off motors - Initial state
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  
    // Set the motor speed
  analogWrite(enA, 0); 
  analogWrite(enB, 0);
  int val0 = digitalRead(ENC_IN_RIGHT_B);
  int val1 = digitalRead(ENC_IN_LEFT_B);
  int val3 = digitalRead(ENC_IN_RIGHT_A);
  int val4 = digitalRead(ENC_IN_LEFT_A);
Serial.begin(9600);
}
void loop() {
//int val = digitalRead(ENC_IN_RIGHT_B);
//Serial.println(val0);
//Serial.println(val1);
//Serial.println(val2);
//Serial.println(val3);
//Serial.println("----------------------------");
 
if(Serial.available()){
  t = Serial.read();
  Serial.println(t);
}
if(t == 'F'){            //
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);
    analogWrite(enA, 140); // FORWARD
  analogWrite(enB, 220);
  //Serial.println(val);
//Serial.println("----------------------------");
  
}
else if(t == 'L'){      //
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);
    analogWrite(enA, 100); 
  analogWrite(enB, 140);
  //Serial.println(val);
//Serial.println("----------------------------");
} 
else if(t == 'B'){      //reverse
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  analogWrite(enA, 100); 
  analogWrite(enB, 140);
  //Serial.println(val);
//Serial.println("----------------------------");
}
else if(t == 'R'){      
  digitalWrite(in1,HIGH);//
  digitalWrite(in2,LOW);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
   analogWrite(enA, 100); 
  analogWrite(enB, 140);
  //Serial.println(val);
//Serial.println("----------------------------");
}

 

else if(t == 'S'){      //STOP (all motors stop)
 digitalWrite(in1,LOW);
  digitalWrite(in2,LOW);
  digitalWrite(in3,LOW);
  digitalWrite(in4,LOW);
  //Serial.println(val);
//Serial.println("----------------------------");
}

                        
}
