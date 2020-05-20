#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <OpenWeatherMap.h>

const char *ow_key = "XXXXXXXXXXXXXXXXXXX";
const char *ssid = "XXXXX";
const char *pass = "XXXXXXXXX";
OWMconditions owCC;
float press_old=0;
float press_new;
bool high_press_flag = false;
bool initialize = false;
#define GREEN_LED 14
#define BLUE_LED 16
#define RED_LED 12

void setup() {
    Serial.begin(9600);
    delay(10);
    WiFi.softAPdisconnect (true);
    pinMode(GREEN_LED, OUTPUT);
    pinMode(BLUE_LED, OUTPUT);
    pinMode(RED_LED, OUTPUT);
}

void currentConditions(void) {
    OWM_conditions *ow_cond = new OWM_conditions;
    owCC.updateConditions(ow_cond, ow_key, "ca", "Toronto", "metric");
    press_new = ow_cond->pressure.toFloat();

    if (press_new > 0)
    {
       if (press_old == 0)
       {
          press_old = press_new;
       }
       if (press_new != press_old)
       {
         initialize = true;
         if (press_new > press_old)
          {
              high_press_flag = true;
          }
          else
          {
              high_press_flag = false;
          }
          pres_old = press_new;
       }
    }

    delete ow_cond;
}

void loop() {
        if (WiFi.status() != WL_CONNECTED) { //wifi not connected?
              WiFi.begin(ssid, pass);
              Serial.println("Connecting to Wi-Fi");
              delay(2000);
          
              if (WiFi.waitForConnectResult() == WL_CONNECTED) {
                  Serial.println("Wi-Fi Connected!");
                  delay(2000);
                  return; 
              } 
        }
        if (WiFi.waitForConnectResult() == WL_CONNECTED) {
                  currentConditions();
                  if (initialize == true)
                  {
                    if (high_press_flag == true)
                    {
                        FlashGreenLED(250, 5);
                    }
                    else
                    {
                        FlashRedLED(100, 10);
                    }
                  }
                  else
                  {
                        FlashBlueLED(500, 5);
                  }          
                  if (press_new > 0)
                  {
                      delay(900000); 
                  }
                  else
                  {
                      delay(10000);
                  }               
                  return; 
         } 
  }

void FlashGreenLED(int delayTime, int numOfFlashes) {
      int var = 0;
      while(var < numOfFlashes ) {
          digitalWrite(BLUE_LED, LOW);
          digitalWrite(RED_LED, LOW);
          digitalWrite(GREEN_LED, LOW);
          delay(delayTime); 
          digitalWrite(GREEN_LED, HIGH); 
          delay(delayTime);
          var++; 
      }
  }

void FlashBlueLED(int delayTime, int numOfFlashes) {
      int var = 0;
      while(var < numOfFlashes ) {
          digitalWrite(GREEN_LED, LOW);
          digitalWrite(RED_LED, LOW);
          digitalWrite(BLUE_LED, LOW);
          delay(delayTime); 
          digitalWrite(BLUE_LED, HIGH); 
          delay(delayTime);
          var++; 
      }
  }

void FlashRedLED(int delayTime, int numOfFlashes) {
      int var = 0;
      while(var < numOfFlashes ) {
          digitalWrite(GREEN_LED, LOW);
          digitalWrite(BLUE_LED, LOW);
          digitalWrite(RED_LED, LOW);
          delay(delayTime); 
          digitalWrite(RED_LED, HIGH); 
          delay(delayTime);
          var++; 
      }
  }