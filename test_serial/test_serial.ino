void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String input_str = Serial.readStringUntil('\n');
    Serial.print("Received: ");
    Serial.println(input_str);
    String response_str = "Response to " + input_str;
    Serial.println(response_str);
  }
}
