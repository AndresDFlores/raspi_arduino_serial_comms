void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  while (!Serial) {}
}

void loop() {

  // // put your main code here, to run repeatedly:
  // Serial.println("Hello from Arduino");
  // delay(1000);

  // Generate a random number between 0 (inclusive) and 100 (exclusive)
  long randomNumber1 = random(100); 
  // Serial.print("Random number (0-99): ");
  Serial.println(randomNumber1);

  // // Generate a random number between 10 (inclusive) and 50 (exclusive)
  // long randomNumber2 = random(10, 50); 
  // Serial.print("Random number (10-49): ");
  // Serial.println(randomNumber2);

  // delay(1000); // Wait for 1 second before generating the next numbers
  delay(10);
}
