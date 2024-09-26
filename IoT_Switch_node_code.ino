/*
 Before upload, check if you have all the libraries installed
 and if the ports and board are configured.
 Created 26.09.2024 by Bohdan Suskyi
*/

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>  // A library for working with JSON

const char* ssid = "**********";  // Replace Wi-Fi with your name
const char* password = "**********";  // Replace with your Wi-Fi password

const char* serverUrl = "http://**********.pythonanywhere.com/create/";  // Replace with the URL of your Django server

unsigned long previousMillis = 0;  // Save the last time the request was sent
const long interval = 1000;  // Interval between requests

const int RelayPin = 4; // D2 (or another PIN)
bool RelayState = false;  // The initial state of the relay

void setup() {
  pinMode(RelayPin, OUTPUT);
  digitalWrite(RelayPin, LOW);  // Turn off the relay (LED) at the start
  Serial.begin(115200);

  WiFi.begin(ssid, password);

  // Non-blocking WiFi connection
  while (WiFi.status() != WL_CONNECTED) {
    Serial.println("Connecting to WiFi...");
    delay(1000);
  }
  
  Serial.println("Connected to WiFi");
}

void loop() {
  unsigned long currentMillis = millis();

  // Non-blocking delay
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;  // Update the last request time

    if (WiFi.status() == WL_CONNECTED) {
      WiFiClient client;
      HTTPClient http;

      // Form a request
      String urlWithParams = String(serverUrl) + "?get_value=" + String(RelayState ? "True" : "False");
      http.begin(client, urlWithParams);  // Open an HTTP request
      
      int httpResponseCode = http.GET();  // Send a GET request

      if (httpResponseCode > 0) {
        String response = http.getString();  // Receive a response from the server
        Serial.println(httpResponseCode);
        Serial.println(response);
        
        // Parse the JSON response
        DynamicJsonDocument doc(1024);
        DeserializationError error = deserializeJson(doc, response);
        
        if (error) {
          Serial.print("JSON Parsing failed: ");
          Serial.println(error.c_str());
          return;
        }

        // Get send_value from JSON
        bool send_value = doc["send_value"];

        // Relay (LED) control based on send_value
        if (send_value) {
          digitalWrite(RelayPin,LOW);  // the relay is off
          RelayState = true;
        } else {
          digitalWrite(RelayPin,HIGH);  // the relay is on
          RelayState = false;
        }

      } else {
        Serial.println("Error in sending GET request");
      }

      http.end();  // Completing the request
    } else {
      Serial.println("WiFi not connected, retrying...");
    }
  }
}
