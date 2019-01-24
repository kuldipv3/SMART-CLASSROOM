// ir1(pin8)->ir2(pin9) counter increase
//black2 purple3
#include<SoftwareSerial.h>

void dweetUpdate(int count);
SoftwareSerial ser(2,3);

int irpin1=8;
int irpin2=9;
int hasObstacle1 = HIGH;
int hasObstacle2 = HIGH;

static int count=0;
String ssid = "verma";
String password = "98109107200";
 


void setup(){
  // put your setup code here, to run once:
pinMode(irpin1,INPUT);
pinMode(irpin2,INPUT);
Serial.begin(9600);
ser.begin(9600);
String wific = "AT+CWJAP=\"";
wific += ssid;
wific += "\",\"";
wific += password;
wific += "\"";
Serial.println(wific);
ser.println(wific);
delay(3000);
ser.println("AT+RST");
delay(1000);
count = 0;
dweetUpdate(count);
}

void loop() {
  // put your main code here, to run repeatedly:
hasObstacle1 = digitalRead(irpin1);
while(hasObstacle1 == 0){
  hasObstacle2 = digitalRead(irpin2);
  if(hasObstacle2 == 0){
    Serial.println("obstacle2 detected after obstacle1\n");
    count++;
    Serial.println(count);
    dweetUpdate(count);
    delay(500);
    break;
  }
  hasObstacle1 = digitalRead(irpin1);
}

hasObstacle2 = digitalRead(irpin2);
while(hasObstacle2 == 0){
  hasObstacle1 = digitalRead(irpin1);
  if(hasObstacle1 == 0){
    Serial.println("obstacle1 detected after obstacle2\n");
    count--;
    if(count<0){
      count=0;
    }
    Serial.println(count);
    dweetUpdate(count);
    delay(500);
    break;
  }
  hasObstacle2 = digitalRead(irpin2);
}
}

void dweetUpdate(int count){
  
  String cmd = "AT+CIPSTART=\"TCP\",\"";
  cmd += "www.dweet.io";
  cmd += "\",80";
  ser.println(cmd);

  if(ser.find("Error")){
  Serial.println("AT+CIPSTART error");
  return;
  }

  //prepare GET string 
  String sendStr = "GET /dweet/for/kv3sc?count=";
  sendStr += String(count);
  sendStr += "\r\n";
  cmd = "AT+CIPSEND=";
  cmd += String(sendStr.length()+8);
  ser.println(cmd);

  if(ser.find(">")){
    ser.print(sendStr);
    ser.println("\r\n");
    ser.println("\r\n");
    Serial.println("SENT");
  }
  else{
    ser.println("AT+CIPCLOSE");
    Serial.println("AT+CIPCLOSE");
  }
  delay(1000);



}
