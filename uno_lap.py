import serial
import time

# Open serial connection
ser = serial.Serial('COM7', 9600)  # Change 'COM3' to your Arduino's port
ser.flushInput()

while True:
    if ser.in_waiting > 0:
        # Read serial data
        line = ser.readline().decode('utf-8').rstrip()

        # Check if data starts with 'Time: '
        if line.startswith('Time: '):
            # Extract time string and remove 'Time: '
            time_str = line[len('Time: '):]
            
            # Print received time
            print("Received time from Arduino:", time_str)

            # Parse time string if needed
            # Example parsing:
            # hour, minute, second = map(int, time_str.split(':'))

    time.sleep(1)
