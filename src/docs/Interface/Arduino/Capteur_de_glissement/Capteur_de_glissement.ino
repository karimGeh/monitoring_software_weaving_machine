#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

// --- Variables globales --- 
int             rpm1,rpm2;                      // La vitesse de rotation
int             RapportDeTransmission;
volatile byte   impulsion1,impulsion2;          // La variable incrémentale
unsigned long   timeold1,timeold2;
unsigned int    pulsos_por_volta1 = 40;    // Le nombre du disque d'encodeur grande poulie
unsigned int    pulsos_por_volta2 = 20;    // Le nombre du disque d'encodeur petite poulie
// ========================================================================================================
 
void compteur1()
{
  impulsion1++;//Incrementation du compteur
}
void compteur2()
{
  impulsion2++;//Incrementation du compteur
}
// ========================================================================================================

void setup()
{
  lcd.begin(16,2);
  lcd.backlight();
  Serial.begin(9600);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  
  //Déclencher le compteur à chaque impulsion
  attachInterrupt(0, compteur1, RISING);
  attachInterrupt(0, compteur2, RISING);
  impulsion1  = 0;
  rpm1        = 0;
  timeold1    = 0;
  impulsion2  = 0;
  rpm2        = 0;
  timeold2    = 0;
} 
// ========================================================================================================

void loop()
{
  lcd.clear();
  if (millis() - timeold1 >= 1000 || millis() - timeold2 >= 1000) //Mettre à jour le compteur toutes les secondes
  {
    detachInterrupt(0);               //Désactiver l'interruption pendant le calcul
    rpm1 = (60 * 1000 / pulsos_por_volta1 ) / (millis() - timeold1) * impulsion1;
    rpm2 = (60 * 1000 / pulsos_por_volta2 ) / (millis() - timeold2) * impulsion2;
    RapportDeTransmission=rpm2/rpm1;
    timeold1 = millis();
    impulsion1 = 0;
    timeold2 = millis();
    impulsion2 = 0;
    Serial.print("RPM 1 = ");           //Afficher la valeur RPM sur le moniteur série
    Serial.println(rpm1, DEC);         //Activer l'interruption
    Serial.print("RPM 2 = ");           //Afficher la valeur RPM sur le moniteur série
    Serial.println(rpm2, DEC);         //Activer l'interruption
    attachInterrupt(0, compteur1, RISING);
    attachInterrupt(0, compteur2, RISING);
    lcd.setCursor (0,1);
    lcd.print("Rapport de transmission=");
    lcd.setCursor (0,2);
    lcd.print(RapportDeTransmission);
    delay(1000);
    lcd.clear();
  }
  
} 
