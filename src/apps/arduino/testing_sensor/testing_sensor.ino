// This code is not for poduction and is only 
// for testing how the python code will read from the arduino

#define SENSOR_ADDR 1


#define TIME_INTERVAL 100.0

int state = 0;
float value = 100.0;
float data;
float data1;
float data2;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  delay(TIME_INTERVAL);
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
