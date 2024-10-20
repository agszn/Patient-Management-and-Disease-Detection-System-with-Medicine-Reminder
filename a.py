import serial
import time

# Configure the serial port
ser = serial.Serial('COM7', 9600)  # Change 'COM3' to the appropriate port
time.sleep(2)  # Wait for the serial connection to establish

# Send signal to Arduino
ser.write(b'start')

# Wait for response from Arduino
response = ser.readline().strip()
if response == b'ready':
    print("Arduino is ready, starting IR sensor...")
    # Now you can start the IR sensor or perform any other actions

# Close the serial connection
ser.close()
