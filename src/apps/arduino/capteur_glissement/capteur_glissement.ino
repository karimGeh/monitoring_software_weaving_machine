#define SENSOR_ADDR 1

#define PIN_MOTOR_1 2
#define PIN_MOTOR_2 3

#define TIME_INTERVAL 500


int encoder_1 = 1, encoder_2 = 1;


void interuptMotor1()
{
  encoder_1++;
}
void interuptMotor2()
{
  encoder_2++;
}

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);

  pinMode(PIN_MOTOR_1, INPUT);
  pinMode(PIN_MOTOR_2, INPUT);

  attachInterrupt(digitalPinToInterrupt(PIN_MOTOR_1), interuptMotor1, RISING);
  attachInterrupt(digitalPinToInterrupt(PIN_MOTOR_2), interuptMotor2, RISING);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(TIME_INTERVAL);
  
  float ct = millis();
  float rapportDeTransmission = ((float) encoder_1) / encoder_2;

  encoder_1 = 1;
  encoder_2 = 1;

  Serial.print(SENSOR_ADDR);
  Serial.print(",");
  Serial.print(ct);
  Serial.print(",");
  Serial.println(rapportDeTransmission);

}
