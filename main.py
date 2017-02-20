from picamera import piCamera
import os
import datetime as dt

cam = piCamera()

def record_video():
    filename = os.path.join(destination, dt.datetime.now().strftime('%Y-%m-%d_%H.%M.%S.h264'))
    camera.start_recording(filename)

def finish_video():
    camera.stop_recording()


record_video()
start_time = dt.datetime.now()
while dt.datetime.now() - start_time < 10:
    pass
finish_video()
