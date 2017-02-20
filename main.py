from picamera import piCamera
import os
import datetime as dt
from time import sleep


cam = piCamera()

sleep(1)
for filename in cam.capture_continuous('img{counter:03d}.jpg'):
    print('Captured %s' % filename)
    sleep(1) # wait 5 minutes
