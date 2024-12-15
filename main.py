from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import time
import socket

SERVER_PRT = 1234
ip_address = "127.0.0.1"  # Use the server's IP address

client = socket.socket()
client.connect((ip_address, SERVER_PRT))

# Initialize the ultrasonic sensor on port D5
SENSOR_PORT = 5
ultrasonic_sensor = GroveUltrasonicRanger(SENSOR_PORT)

try:
    while True:
    
        distance = ultrasonic_sensor.get_distance()
        print(f"Distance: {distance:.2f} cm")

        # Detect objects closer than 30 cm (about 12 inches/1 ft)
        if distance < 30:
            print("Object detected in blind spot")
        
        # Send the distance data to the server
        send_time = time.time()  
        message = f"{distance:.2f}"
        client.send(message.encode())  
        
    
        response = client.recv(1024).decode()
        print(f"Server Response: {response}")

        #round-trip time for performance measures
        rtt = time.time() - send_time
        print(f"Round-trip time: {rtt:.4f} sec")

        time.sleep(0.8)

except KeyboardInterrupt:
    print("Exiting")
    client.close()
