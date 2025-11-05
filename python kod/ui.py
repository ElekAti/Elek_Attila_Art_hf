import serial

PORT = 'COM3'
BAUDRATE = 115200

ser = serial.Serial(PORT, BAUDRATE, timeout=1)
print(f"Connected to {PORT} port")

while True:
    try:
        value = input("Delay (or q for quit): ")
        if value.lower() == 'q':
            print("Exit")
            break
        if not value.isdigit():
            print("Input error")
            continue

        ser.write((value + '\n').encode()) 
        print(f"Send: {value} ms")

    except KeyboardInterrupt:
        break

ser.close()
