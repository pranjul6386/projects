#include "DHT.h"
#include "ESP_MICRO.h" 




#define pinA 5  //D1
#define pinB 4   //D2
#define pinC 0   //D3
#define flame 2  //D4
#define humidity 14 //D5 



int flame_data = 0;
int smoke_data = 0;
int temp_data = 0;
int humidity_data = 0;
int soil_moisture_data = 0;

const int analog_pin = A0;


DHT dht(humidity, DHT11);



void setup(){

  Serial.begin(57600);
  
  start("USERNAME","PASSWORD");  // EnAIt will connect to your wifi with given details

  pinMode(pinA, OUTPUT);
  pinMode(pinB, OUTPUT);
  pinMode(pinC, OUTPUT);
  
  
  pinMode(flame, INPUT);
  
  dht.begin();
  
  
}
void loop(){
    waitUntilNewReq();  //Waits until a new request from python come
  
  
//send FLAME data
  if (getPath()=="/flame"){

    flame_data = digitalRead(flame);
    Serial.println(flame_data);
    if (flame_data == 0)
        {
          returnThisFloat(1);
        }

        else if(flame_data == 1)
        {
          returnThisFloat(0);
        }
      
      
    
  }




//send HUMIDITY data
else if(getPath() == "/humidity"){

  humidity_data = dht.readHumidity();
  Serial.println(humidity_data);
  returnThisFloat(humidity_data);
  
  
}



//send SMOKE data
  else if(getPath() == "/smoke"){

      digitalWrite(pinA, LOW);
      digitalWrite(pinB, LOW);
      digitalWrite(pinC, LOW);


      smoke_data = analogRead(analog_pin);
      if(smoke_data>430){
        Serial.println(1);
        returnThisFloat(1);
        
      }

      else{
         Serial.println(0);
        returnThisFloat(0);
       
      }

      
    
  }


//send TEMP data
  else if(getPath() == "/temp"){

      digitalWrite(pinA, LOW);
      digitalWrite(pinB, LOW);
      digitalWrite(pinC, HIGH);

      temp_data = (analogRead(analog_pin)*330/1024);
        Serial.println(temp_data);

      returnThisFloat(temp_data);
    
      
    
  }




//send SOIL_MOISTURE data
  else if(getPath() == "/soil_moisture"){

      digitalWrite(pinA, LOW);
      digitalWrite(pinB, HIGH);
      digitalWrite(pinC, LOW);

      soil_moisture_data = analogRead(analog_pin);
      Serial.println(soil_moisture_data);

      returnThisFloat(soil_moisture_data);
      
  }
  
}
