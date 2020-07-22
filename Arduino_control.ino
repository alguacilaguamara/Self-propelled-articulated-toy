/* Declaracion de los pines */

int pinPWM_dcha = 6;
int pinPWM_dcha_reverse = 10;
int pinPWM_izda = 5;
int pinPWM_izda_reverse = 11;
int pinReboteUltrasonico = 8;
int pinPulsoUltrasonico = 9;
int pinLED_azul1 = 4;
int pinLED_azul2 = 4;
int pinLED_amarillo_izda = 2;
int pinLED_amarillo_dcha = 11;
int pinLED_rojo1 = 12;
int pinLED_rojo2 = 12;


long distancia;
long tiempo;
void setup(){
  Serial.begin(9600);
  /*activación del pin 9 como salida: para el pulso ultrasónico*/
  pinMode(pinPulsoUltrasonico, OUTPUT);
  /*activación del pin 8 como entrada: tiempo del rebote del ultrasonido*/
  pinMode(pinReboteUltrasonico, INPUT);
  pinMode(pinPWM_izda, OUTPUT);
  pinMode(pinPWM_dcha, OUTPUT);
  pinMode(pinLED_amarillo_izda, OUTPUT);
  pinMode(pinLED_amarillo_dcha, OUTPUT);
}

void adelante(){
  analogWrite(pinPWM_izda, 130);
  analogWrite(pinPWM_dcha, 140);
}

void adelante_calibre(){
  analogWrite(pinPWM_izda, 160);
  analogWrite(pinPWM_dcha, 130);
}

void adelante_rapido(){
  analogWrite(pinPWM_izda, 200);
  analogWrite(pinPWM_dcha, 220);
}

void izda(){
  analogWrite(pinPWM_izda, 150);
  analogWrite(pinPWM_dcha, 0);
  analogWrite(pinPWM_dcha_reverse, 150);
}

void dcha(){
  analogWrite(pinPWM_dcha, 150);
  analogWrite(pinPWM_izda, 0);
  analogWrite(pinPWM_izda_reverse, 150);
}

void parar(){
  analogWrite(pinPWM_izda, 0);
  analogWrite(pinPWM_dcha, 0);
}

void loop(){
  digitalWrite(pinPulsoUltrasonico,LOW); /* Por cuestión de estabilización del sensor*/
  delayMicroseconds(5);
  digitalWrite(pinPulsoUltrasonico, HIGH); /* Envío del pulso ultrasónico*/
  delayMicroseconds(10);

  tiempo=pulseIn(pinReboteUltrasonico, HIGH);

  /* Función para medir la longitud del pulso entrante. Mide el tiempo que transcurrido entre el envío
  del pulso ultrasónico y cuando el sensor recibe el rebote, es decir: desde que el pin 12 empieza a recibir el rebote, HIGH, hasta que
  deja de hacerlo, LOW, la longitud del pulso entrante*/

  distancia= int(0.017*tiempo);

  /* Fórmula para calcular la distancia obteniendo un valor entero*/
  /*Monitorización en centímetros por el monitor serial*/
  Serial.println("Distancia ");
  Serial.println(distancia);
  Serial.println(" cm");
  delay(200);

  digitalWrite(pinLED_azul1, HIGH);
  digitalWrite(pinLED_azul2, HIGH);

  if(distancia < 40)
    digitalWrite(pinLED_amarillo_izda, HIGH);
  else
    digitalWrite(pinLED_amarillo_izda, LOW);

}
