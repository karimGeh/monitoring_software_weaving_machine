#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

byte Encodeur = 6;
int  N  = 0;            //Signal delivré par l'encodeur (O ou 1)
int  n  = 0;            //Incremental à chaque pas du disque d'encodeur 
int  p  = 0;            //Le nombre de tours du disque
int  L  = 0;            //La longueur tissé

void setup()
{
  Serial.begin(9600);
  pinMode(Encodeur, INPUT);
} 

void loop() {
  N=digitalRead(Encodeur);
  if(N!=0){
  n++;
    if(n==15){
         p++;
         L=p*31.4;
         n=0;   
     }
    
  Serial.print("Nombre de tours = ");           //Afficher le nombre de tours
  Serial.println(p, DEC);
  Serial.print("La longeur tissée = ");         //Afficher la longueur tissée
  Serial.println(L, DEC);
  delay(1000);}
 
 
}
