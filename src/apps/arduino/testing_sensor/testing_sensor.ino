// This code is not for poduction and is only 
// for testing how the python code will read from the arduino

#define SENSOR_ADDR 2


#define PIN_RELAY 7
#define TIME_INTERVAL 500.0

int state = 0;
float value = 100.0;
float data;
float data1;
float data2;

void setup()
{
  pinMode(PIN_RELAY, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  delay(TIME_INTERVAL);


  if (Serial.available() > 0)
  {
    int choice = Serial.read() - '0';
    if (choice == 1)
    {
      digitalWrite(PIN_RELAY, HIGH);
    }else if (choice == 0){
      digitalWrite(PIN_RELAY, LOW);
    }
  }


  data = random(-2,3); // generate the integers
  // data2 = random(0, 100); // generate the numbers after the decimal point
  
  // data = data1;// + data2 / 100;
  value += data;
  value = constrain(value, 0, 255);

  // get time
  float ct = millis();
  
  Serial.print(SENSOR_ADDR);  
  Serial.print(",");  
  Serial.print(ct);  
  Serial.print(",");  
  Serial.println(value);

}
