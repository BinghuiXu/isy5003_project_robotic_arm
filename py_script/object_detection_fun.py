import cv2
import pyrealsense2 as rs
import numpy as np
import subprocess
import json
import time
from PIL import Image, ImageDraw, ImageFont


def take_pictures():
    # Configure depth and color streams
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    
    # Start streaming
    pipeline.start(config)
    
    time.sleep(2)

    # Set exposure time (ms)
    exposure_time = 1000
    # exposure_time = 100
    sensor = pipeline.get_active_profile().get_device().first_color_sensor()
    sensor.set_option(rs.option.exposure, exposure_time)

    
    # Wait for a coherent pair of frames: depth and color
    frames = pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()
    # if not color_frame:
    #     continue

    # Convert images to numpy arrays
    color_image = np.asanyarray(color_frame.get_data())



    cv2.imshow('RealSense', color_image)

    cv2.waitKey(3000)


    cv2.imwrite("/home/issuser/5003_course_project/5003/py_script/" +
                          "input_image.jpg", color_image)
    print("save " + "input_image" + ".jpg successfuly!")

    # close opencv window
    cv2.destroyAllWindows()
    
    # Stop streaming
    pipeline.stop()
    
    

    


def object_detection():
    # get object dection api 
    command = 'base64 input_image.jpg | curl -d @- "https://detect.roboflow.com/test-strip-head/2?api_key=dlY8SEPO7DYJU1yGGQdE"'
    output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    response, error = output.communicate()

    response = response.decode('utf-8')
    # print(response)
    image = Image.open('input_image.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('FreeMonoBold.ttf', size=20)

    # separate variables
    data = json.loads(response)
    # print(data)

    if len(data['predictions'])!=0:
        image_sizes=data['image']
        for image_size in image_sizes:
            width_image = image_sizes['width']
            height_image = image_sizes['height']

        predictions = data['predictions']
        for prediction in predictions:
            x = prediction['x']
            y = prediction['y']
            width = prediction['width']
            height = prediction['height']
            confidence = prediction['confidence']
            class_name = prediction['class']
            # print(width_image,height_image,x, y, width, height, confidence, class_name)
            left = x - width / 2
            top = y - height / 2
            right = x + width / 2
            bottom = y + height / 2
                
            draw.rectangle((left, top, right, bottom), outline='red', width=3)
            draw.text((left, top - 20), f'{confidence:.2f}', fill='red',font=font)
    else:    
        image.show()
        return None

    image.show()
    image.save('output_image.png')
    
    return [x,y]

# take_pictures()
# result=object_detection()
# print(result)
# print(f"x:{result[0]},y:{result[1]}")