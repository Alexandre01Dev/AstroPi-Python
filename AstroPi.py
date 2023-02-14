from picamera import PiCamera
from time import sleep
import os
from collections import namedtuple

from orbit import ISS, ephemeris 
from skyfield.api import load
import csv


camera = PiCamera()
camera.resolution = (4056, 3040)
camera.rotation = 90

  # Take a picture every minute for 3 hours

#free = st.f_bavail * st.f_frsize
  
def IsDayTime():
    timescale = load.timescale()
    t = timescale.now()

    if ISS.at(t).is_sunlit(ephemeris):
        print('Sun')
        return True
    else:
        print('Dark')
        sleep(5)
        return False
    
def EnoughStorage():
    st = os.statvfs('/')
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    #total = 24000000000
    used = (st.f_blocks - st.f_bfree) * st.f_frsize

    print(str(used)+'/'+ str(total))
    resultat = total/used
    pourcentage = int(100/resultat)
    print(str(pourcentage)+ '%')
    if(pourcentage <= 98):
        return True
    else:
        return False
    
i = 0
enough_space = True
camera.start_preview()


while(EnoughStorage()):
    i += 1
    
    if IsDayTime() != True:
        continue
    
    #Take pictures
    camera.capture('Image_'+str(i)+'.jpg')



print("while breaked")
#camera.start_preview()

#camera.start_recording('movie.mp4')
#camera.wait_recording(15)
#camera.stop_recording()
sleep(5)

#camera.stop_preview()

