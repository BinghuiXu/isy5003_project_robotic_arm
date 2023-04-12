import serial
import time
from object_detection_fun import take_pictures, object_detection
    


ser = serial.Serial('/dev/ttyACM0', 9600) 



def input_position(input_string):
    print("running to position function")
    ser.write((input_string + "\n").encode()) 
    response = ser.readline() 
    print("now moving: " + response.decode()) 
    time.sleep(5)
    

time.sleep(15)


# on the taking picture position
input_position("250,0,-30,90,10,1000")

# get the position
# take_pictures()
# teststrip_place=object_detection()
# print(teststrip_place)
# new_x = -0.5*teststrip_place[1] + 510
# new_y = (2/7)*teststrip_place[0] -140
new_x = 327.6
new_y = -47.0   
print(new_x,new_y)




# go to the new position
new_position="{:.2f},{:.2f},-40,90,10,1000".format(new_x, new_y)
print(new_position)
time.sleep(15)

input_position(new_position)



# x:511.5,y:155.0  380,-10,-40,90,10,1000 380

# x:463.0,y:60.5   

# x:503.0,y:142.5   370,0,-40,90,10,1000 370

# x:432.0,y:200.5   365,0,-40,90,10,1000


'''
# x:490.0,y:300----  360,0,-20,90,10,1000


# x:421.0,y:290.0---  370,-20,-20,90,10,1000

# x:468.5,y:256.5---  380,-10,-20,90,73,1000
'''



