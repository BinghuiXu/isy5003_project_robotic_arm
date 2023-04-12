import serial
import time
from object_detection_fun import take_pictures, object_detection
    


ser = serial.Serial('/dev/ttyACM0', 9600) # 打开串行端口，根据需要修改端口名称和波特率
time.sleep(15)

new_x=331.75
new_y=-12.71
input_string="{:.2f},{:.2f},-20,90,10,1000".format(new_x, new_y)

print("running to position function")
ser.write((input_string + "\n").encode()) # 将字符串转换为字节并发送到串行端口
response = ser.readline() # 从串行端口读取一行字符串
print("now moving: " + response.decode()) # 将字节转换为字符串并输出
# time.sleep(5)