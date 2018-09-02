void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

int cont = 0;

void loop() {
  // put your main code here, to run repeatedly:
  Serial.write(++cont);
  delay(500);
}
