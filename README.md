Blind Spot Detector with Raspberry Pi
This project uses a Raspberry Pi and an Ultrasonic Sensor (HC-SR04) to create a basic blind spot detection system. When an object is detected by the ultrasonic sensor, an action is triggered on the software.
Prerequisites

Before you begin, make sure you have the following:
Hardware:

    Raspberry Pi (any model with GPIO support)
    HC-SR04 Ultrasonic Sensor
        VCC: Power (5V)
        GND: Ground
        TRIG: Trigger pin (to send a pulse)
        ECHO: Echo pin (to measure the reflected pulse)

Software:

    Python 3
    RPi.GPIO library (for controlling GPIO pins)

Setup Instructions
1. Install Required Software

Make sure to run this on a Raspberry Pi - ensure Python and the necessary library are installed:

    Install RPi.GPIO (if not already installed):
    sudo apt update
    sudo apt install python3-rpi.gpio

    This library will allow you to interact with the GPIO pins of the Raspberry Pi.

2. Connect the Ultrasonic Sensor to the Raspberry Pi

Here’s the wiring guide for the HC-SR04 ultrasonic sensor:
HC-SR04 : Pin	Raspberry Pi Pin
VCC	- 5V (pin 2)
GND	- GND (pin 6)
TRIG - GPIO 23 (pin 16)
ECHO -	GPIO 24 (pin 18)
