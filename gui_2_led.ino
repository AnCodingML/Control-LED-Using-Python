//KONTROL 2 LED MENGGUNAKAN PC

int LED1 = 13;
int LED2 = 12;
int out;

void setup()
{
  Serial.begin(9600);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT); 
}

void loop()
{
  if (Serial.available()>0)
  {
    int baca = Serial.read();
    if (baca == 'a')
    {
      digitalWrite(LED1, HIGH);
      Serial.print("LED1 NYALA");
    }
    if (baca == 'b')
     {
      digitalWrite(LED1, LOW);
      Serial.print("LED1 MATI");
     }
    if (baca == 'c')
     {
      digitalWrite(LED2, HIGH);
      Serial.print("LED2 NYALA");
     }
     if (baca == 'd')
     {
      digitalWrite(LED2, LOW);
      Serial.print("LED2 MATI");
     }
    
    
  }
}
