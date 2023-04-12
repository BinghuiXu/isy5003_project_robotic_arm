import serial
import time

    


ser = serial.Serial('/dev/ttyACM0', 9600) # 打开串行端口，根据需要修改端口名称和波特率



def input_position(input_string):
    print("running to position function")
    ser.write((input_string + "\n").encode()) # 将字符串转换为字节并发送到串行端口
    response = ser.readline() # 从串行端口读取一行字符串
    print("now moving: " + response.decode()) # 将字节转换为字符串并输出
    time.sleep(5)
    
    
# #main loop
# while True:
#     response = ser.readline() # 从串行端口读取一行字符串
#     print("Response: " + response.decode()) # 将字节转换为字符串并输出
#     if (response.decode()).strip=="initial done":
#         print("out of initial loop")
#         break

time.sleep(15)
# on top of test strip
input_position("315,-60,150,90,10,1000")


# position before take new test strip
input_position("315,-60,-20,90,10,1000")


# position to take new test strip
input_position("315,-60,-20,90,73,1000")

# after removing new test strip
input_position("315,-60,150,90,73,1000")


# on top of water container
input_position("340,140,150,90,73,1000")


#  into water container
input_position("340,140,-25,90,73,1000")


#  bring out from water container
input_position("340,140,150,90,73,1000")
# time.sleep(120000)


#  straight up
input_position("180,90,90,90,73,390")


#  move to the camera before take picture
# go low
input_position("0,340,250,90,73,1000")
# lower
input_position("0,340,150,180,73,1000")

#  move beneath the camera
# go parallel
input_position("0,550,50,0,73,100")

#  move beneath the camera
input_position("0,550,50,0,73,100")
time.sleep(90)

# #  straight up
# input_position("180,90,90,90,73,390")



#  go back
# input_position("0,450,150,0,73,1000")
# input_position("0,340,250,90,73,1000")
input_position("180,90,90,90,73,390")

# discard test strip
input_position("325,-300,150,90,73,1000")
input_position("325,-300,-100,90,73,1000")
input_position("325,-300,-100,90,10,1000")

# straight up again
input_position("90,90,90,90,73,390")





