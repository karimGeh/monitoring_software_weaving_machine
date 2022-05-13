// This code is not for poduction and is only 
// for testing how the python code will read from the arduino

#define SENSOR_ADDR 2


#define TIME_INTERVAL 50.0

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
  if (Serial.available() > 0)
  {
    int choice = Serial.read() - '0';
    if (choice == 1)
    {
      state = 1;
    }
    if (choice == 0)
    {
      state = 0;
    }
  }


  if(state == 1){
    data1 = random(0, 6)-3; // generate the integers
    // data2 = random(0, 100); // generate the numbers after the decimal point
    data = data1;// + data2 / 100;
    value += data;
    value = constrain(value, 0, 255);

    // get time
    float ct = millis();
    Serial.print(ct);  
    Serial.print(",");  
    Serial.println(value);
  } else {
    Serial.println(SENSOR_ADDR);
  }

}
