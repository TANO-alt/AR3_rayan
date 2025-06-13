#include <Servo.h>

const int VRx = A0;
const int SW = 4;
Servo monServo;

int mode = 0; // 0 = interface Python, 1 = joystick
int valJoystick = 0;
int servoOutput = 90;

void setup() {
  Serial.begin(9600);
  pinMode(VRx, INPUT);
  pinMode(SW, INPUT_PULLUP);
  monServo.attach(9);
  monServo.write(90);
}

void loop() {
  // Lecture série depuis Python
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    input.trim();

    if (input.startsWith("V")) {
      int val = input.substring(1).toInt();
      if (mode == 0) { // Accepte les commandes que si en mode Python
        monServo.write(val);
      }
    } else if (input == "MODE_JOY") {
      mode = 1;
    } else if (input == "MODE_PY") {
      mode = 0;
      monServo.write(90); // Stop au changement
    }
  }

  // Si joystick actif
  if (mode == 1) {
    valJoystick = analogRead(VRx);
    servoOutput = map(valJoystick, 0, 1023, 0, 180);
    if (servoOutput > 85 && servoOutput < 95) {
      servoOutput = 90;
    }
    monServo.write(servoOutput);
  }

  delay(50);
}
