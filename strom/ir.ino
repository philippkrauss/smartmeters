

#define IR_OUT 2
#define IR_IN 7
#define LOGIC_POWER_OUT 12
#define LOGIC_GROUND_OUT 11
#define SIGNAL_OUT 10

#define THRESHOLD 460

void setup() {
//  Serial.begin(9600);
  pinMode(IR_OUT, OUTPUT);
  pinMode(LOGIC_POWER_OUT, OUTPUT);
  pinMode(LOGIC_GROUND_OUT, OUTPUT);
  pinMode(SIGNAL_OUT, OUTPUT);
  digitalWrite(LOGIC_POWER_OUT, HIGH);
  digitalWrite(LOGIC_GROUND_OUT, LOW);
  digitalWrite(SIGNAL_OUT, LOW);
}

void loop() {
  digitalWrite(IR_OUT, HIGH);
  delay(10);
  int readWithLed = analogRead(IR_IN);
  digitalWrite(IR_OUT, LOW);
//  Serial.print(readWithLed);
//  Serial.print(",");
//  int status = 0;
  if (readWithLed < THRESHOLD) {
//    status = 700;
    digitalWrite(SIGNAL_OUT, HIGH);
  } else {
    digitalWrite(SIGNAL_OUT, LOW);
  }
//  Serial.println(status);
  delay(40);
}