import serial
import time
# arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)
# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data
# while True:
#     num = input("Enter a number: ") # Taking input from user
#     value = write_read(num)
#     print(value) # printing the value
    


ser = serial.Serial('/dev/ttyACM0', 9600) # 打开串行端口，根据需要修改端口名称和波特率

while True:
    input_str = input("Enter a message: ")
    ser.write((input_str + "\n").encode()) # 将字符串转换为字节并发送到串行端口
    response = ser.readline() # 从串行端口读取一行字符串
    print("Response: " + response.decode()) # 将字节转换为字符串并输出
