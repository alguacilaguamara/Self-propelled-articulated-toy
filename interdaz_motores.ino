// Configuramos los pines que vamos a usar
int motorDer1=2;//El pin 2 a In1 del L298N
int motorDer2=3;//El pin 3 a In2 del L298N
int motorIzq1=7;//El pin 7 a In3 del L298N
int motorIzq2=4;//El pin 4 a In4 del L298N
int derecho=5;  //El pin 5 a EnA del L298N
int izquierdo=6;//El pin 6 aEnB del L298N

int velocidad=150;

void setup()
{
  //Configuramos los pines como salida
  pinMode(motorDer1, OUTPUT);
  pinMode(motorDer2, OUTPUT);
  pinMode(motorIzq1, OUTPUT);
  pinMode(motorIzq2, OUTPUT);
  pinMode(derecho, OUTPUT);
  pinMode(izquierdo, OUTPUT);

}
void atras(){
  digitalWrite(motorDer1,HIGH);
  digitalWrite(motorDer2,LOW);
  digitalWrite(motorIzq1,HIGH);
  digitalWrite(motorIzq2,LOW);
  analogWrite(derecho,200);//Velocidad motor
  analogWrite(izquierdo,200);
}
void adelante(){
  digitalWrite(motorDer1,LOW);
  digitalWrite(motorDer2,HIGH);
  digitalWrite(motorIzq1,LOW);
  digitalWrite(motorIzq2,HIGH);
  analogWrite(derecho,200);
  analogWrite(izquierdo,200);
}
void giraDerecha(){
  digitalWrite(motorDer1,HIGH);
  digitalWrite(motorDer2,LOW);
  digitalWrite(motorIzq1,LOW);
  digitalWrite(motorIzq2,HIGH);
  analogWrite(derecho,200);
  analogWrite(izquierdo,200);
}
void giraIzquierda(){
  digitalWrite(motorDer1,LOW);
  digitalWrite(motorDer2,HIGH);
  digitalWrite(motorIzq1,HIGH);
  digitalWrite(motorIzq2,LOW);
  analogWrite(derecho,200);
  analogWrite(izquierdo,200);
}
void parar(){
  digitalWrite(motorDer1,LOW);
  digitalWrite(motorDer2,LOW);
  digitalWrite(motorIzq1,LOW);
  digitalWrite(motorIzq2,LOW);
  analogWrite(derecho,200);
  analogWrite(izquierdo,200);
}

void loop() {
       adelante();
       delay(3000);
       atras();
       delay(3000);
       giraDerecha();
       delay(3000);
       giraIzquierda();
       delay(3000);
       parar();
       delay(3000);
  }
