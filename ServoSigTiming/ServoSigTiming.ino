unsigned long duration;
int signalPin = 7;
int outPin = 4;

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(signalPin, INPUT);
  pinMode(outPin, OUTPUT);
}

void loop()
{
  duration = pulseIn(signalPin, HIGH);
  Serial.print(duration);
  if(duration > 1515)
  {
    digitalWrite(outPin, HIGH);
    Serial.println("ON");
  }
  else
  {
    digitalWrite(outPin, LOW);
    Serial.println("OFF");
  }
}
