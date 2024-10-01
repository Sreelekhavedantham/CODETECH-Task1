// Define the pin for the LED
const int ledPin = 13; // Pin where the LED is connected

void setup() {
 pinMode(ledPin, OUTPUT);
}
void loop() {
  // Turn the LED on
  digitalWrite(ledPin, HIGH);
  // Wait for one second (1000 milliseconds)
  delay(1000);
  // Turn the LED off
  digitalWrite(ledPin, LOW);
  // Wait for one second
  delay(1000);
}
