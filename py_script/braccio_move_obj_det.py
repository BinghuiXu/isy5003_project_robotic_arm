import serial
import time
from object_detection_fun import take_pictures, object_detection
from tagui import *
    


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
take_pictures()
teststrip_place=object_detection()
print(teststrip_place)



def calculate_position(teststrip_place):
    # new_x = -0.5*teststrip_place[1] + 510
    # new_y = (2/7)*teststrip_place[0] -140
    new_x = -0.45*teststrip_place[1] + 451
    # new_y = 1*teststrip_place[0] - 490  
    new_y = 0.45*teststrip_place[0] - 212.25 +15  
    # print(new_x,new_y)
    return [new_x,new_y]

def go_catch(x_y):
    # refresh the status
    input_position("315,-60,150,90,10,1000")
    # go to the new position
    new_position="{:.2f},{:.2f},-45,90,10,1000".format(x_y[0],x_y[1])
    print(new_position)
    # time.sleep(5)
    input_position(new_position)


    # grab the test strip first time
    new_position="{:.2f},{:.2f},-45,90,71,1000".format(x_y[0],x_y[1])
    print(new_position)
    input_position(new_position)


    # grab the test strip up
    new_position="{:.2f},{:.2f},100,90,71,1000".format(x_y[0],x_y[1])
    print(new_position)
    input_position(new_position)

x_y=calculate_position(teststrip_place)
go_catch(x_y)


input_position("250,0,-30,90,71,1000")
take_pictures()
teststrip_place_2=object_detection()
while teststrip_place_2!=None:
    x_y=calculate_position(teststrip_place_2)
    go_catch(x_y)
    input_position("250,0,-30,90,71,1000")
    take_pictures()
    teststrip_place_2=object_detection()
    print(teststrip_place_2)
    

url = "http://localhost:3000/"
open_browser()
navigate(url)

refresh_page()



















# x:511.5,y:155.0  380,-10,-40,90,10,1000 380

# x:463.0,y:60.5   

# x:503.0,y:142.5   370,0,-40,90,10,1000 370

# x:432.0,y:200.5   365,0,-40,90,10,1000

# 465 208           365,0,-40,90,10,1000
# 482 186
# 494 204
# 505 341           305,15,-40,90,10,1000
# 514.5, 340.5
# 535.5, 168.0      375.40,80,-50,90,10,1000
# 546.5, 415.0      285,0,-45,90,10,1000

# 481.0, 397.0      272.35,19.20,-45,90,10,1000

'''
# x:490.0,y:300----  360,0,-20,90,10,1000


# x:421.0,y:290.0---  370,-20,-20,90,10,1000

# x:468.5,y:256.5---  380,-10,-20,90,73,1000
'''



