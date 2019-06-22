# SMART-CLASSROOM
The main objective of this project is to develop a Smart Classroom Prototype using an Arduino and Raspberry Pi.

As technology is advancing so schools are also getting smarter. Modern Schools are gradually shifting from conventional switches to centralized control system, involving remote controlled switches. Presently, conventional wall switches located in different parts of a classroom makes it difficult for the user to go near them to operate. 

In order to achieve this , IR Modules are interfaced to the Arduino Board,which count the number of students present in class and uploads the data to cloud using ESP8266 . The Raspberry Pi recieves the data from the cloud and controls the indivisual light and fan zones of a classroom.The loads are operated by Raspberry Pi board through Relay. A master switch is also present on Adafruit which can be accessed by the Teacher.

# Hardware and Software

Raspberry Pi

Raspbian OS

Python - Libraries - RPi, Adafruit IO, JSON

Arduino

Arduino IDE - Libraries - SoftwareSerial

ESP8266 Wifi Module

IR Module

Relay Module


# Working

The prototype replaces the relay with LED for demonstration purpose as the operating
code for relay and LED is the same. For live project use Relay Instead of LED as given
in circuit diagram.

When the IR’s on the Arduino detect a motion from Right to Left,in this case motion of
hand, the counter on cloud gets incremented by one. This is the number of students
present in the class. The raspberry pi retrieves the data from cloud and determines the
zone in which the light and fan is to be switched on, in the case of this prototype the LEDs represent the light. Presently the code is optimized for 8 students to be sit in pairs.
It can be tweaked easily according to the strength of a classroom.

As this system is wireless ,the Arduino curcuit can be implied on the door and the
Raspberry Pi can be used to control the electrical circuit of the classroom.

![alt text](https://github.com/kuldipv3/SMART-CLASSROOM/blob/master/github.png "Working Images")

A master switch is also created using MQTT and Adafruit. The raspberry pi subscribes to
a particular feed called Master Switch on the broker, Adafruit cloud. The Pi keeps
checking the broker for any change in status of Master Switch.
As soon as the broker publishes ON status to Master switch, the client i.e Raspberry Pi
overrides the counter logic and switches on all LEDs (which represnt the actual lights in
a classroom).


# Future expansion of this project

Face detection attendance system

Speech Recognition of Teacher to create text notes

