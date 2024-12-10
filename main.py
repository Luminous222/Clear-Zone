import RPi.GPIO as GPIO
import time

# GPIO Mode (BCM or BOARD)
GPIO.setmode(GPIO.BCM)

# Set GPIO pins
TRIG = 23
ECHO = 24

# Set GPIO direction (IN / OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def measure_distance():
    # Send a short pulse to trigger
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # 10µs pulse
    GPIO.output(TRIG, False)

    # Measure response time
    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    # Time difference to distance
    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2  # cm
    return distance

try:
    while True:
        dist = measure_distance()
        print(f"Distance: {dist:.2f} cm")
        
        # Detect objects closer than 30 cm
        if dist < 30:
            print("Object detected in blind spot!")
        
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Cleaning up before exiting.")
    GPIO.cleanup()

