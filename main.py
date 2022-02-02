#!/usr/bin/python
# -*- coding:utf-8 -*-

import SSD1306
import PCA9685
import time
import traceback
import socket
import threading
import os
from PIL import Image,ImageDraw,ImageFont

try:
        oled = SSD1306.SSD1306()

        pwm = PCA9685.PCA9685(0x40, debug=False)
        pwm.setPWMFreq(50)
        pwm.setServoPulse(0,100)

        # Initialize library.
        oled.Init()
        oled.ClearBlack()

        # Create blank image for drawing.
        image1 = Image.new('1', (oled.width, oled.height), "WHITE")
        draw = ImageDraw.Draw(image1)
        font = ImageFont.load_default()
        while(1):
                draw.rectangle((0,0,128,32), fill = 1)
                # get ip
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(('8.8.8.8', 80))
                localhost = s.getsockname()[0]
                print("ip:%s" %localhost)
                draw.text((0,0), "IP:", font=font, fill = 0)
                draw.text((20,0), localhost, font=font, fill = 0)

                # get temp
                draw.text((0,16), "Temp(Celsius):", font=font, fill = 0)
                file = open("/sys/class/thermal/thermal_zone0/temp")
                temp = float(file.read()) / 1000.00
                temp = float('%.2f' % temp)
                file.close()
                print("temp : %.2f" %temp)
                draw.text((85,16), str(temp), font=font, fill = 0)

                if(temp > 40):
                        pwm.setServoPulse(0,10)
                elif(temp > 50):
                        pwm.setServoPulse(0,50)
                elif(temp > 55):
                        pwm.setServoPulse(0,75)
                elif(temp > 60):
                        pwm.setServoPulse(0,90)
                elif(temp > 65):
                        pwm.setServoPulse(0,100)
                else:
                        pwm.setServoPulse(0,0)
                #show
                oled.ShowImage(oled.getbuffer(image1.rotate(180)))
                time.sleep(1)



except IOError as e:
    oled.Closebus()
    print(e)

except KeyboardInterrupt:
    print("ctrl + c:")
    oled.Closebus()
