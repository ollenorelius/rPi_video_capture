from picamera import PiCamera
import os
import datetime as dt
from time import sleep
import sys

cam = PiCamera()
folder = sys.argv[1]
sleep(1)

if not os.path.exists('./%s'%folder):
    os.makedirs('./%s'%folder)

cam.sensor_mode = 5
cam.shutter_speed = 10000

for filename in cam.capture_continuous('%s/img{counter:03d}.jpg'%folder,use_video_port=True):
    print('Captured %s' % filename)
    sleep(0.5)
    #input()
