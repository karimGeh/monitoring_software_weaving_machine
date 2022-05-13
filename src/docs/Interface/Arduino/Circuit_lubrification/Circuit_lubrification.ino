//Capteur de la longueur tissée
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

byte Encodeur_Roulement = 8;
byte Pompe = 12;
int  N2  = 0;
int  n2  = 0;
int  p2  = 0;  

void setup()
{
  Serial.begin(9600);
  pinMode(Pompe, OUTPUT);
  pinMode(Encodeur_Roulement, INPUT);
  
} 

void loop() {
  N2=digitalRead(Encodeur_Roulement);
  if(N2!=0){
  n2++;
    if(n2==15){
         p2++;
         n2=0;   
         if(p2==1000){
          digitalWrite(Pompe, HIGH);
         }
     }
    
  Serial.print("Nombre de tours = ");           //Afficher le nombre de tours
  Serial.println(p2, DEC);
  delay(1000);}
 
 
}
