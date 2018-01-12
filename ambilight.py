from __future__ import print_function
from colour import Color
from math import sqrt
#Python tv watcher
import picamera
import picamera.array
from fractions import Fraction
from colors import *
import pyphue
myHue = pyphue.PyPHue(ip='192.168.0.157',user='DuuwppZiNJCneZcgQQs-01ckob4yjYnHw0UmoM0V')



xsize =  128
ysize=96
tvwidth=26
tvheight=19 
tvx=42
tvy=37

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as output:
        camera.rotation = 180
        camera.resolution=(xsize,ysize)
        camera.exposure_compensation = 25
        camera.capture(output,'rgb')
        print('Captured %d x %d image' % (output.array.shape[1], output.array.shape[0]))

        red=0
        green=0
        blue=0

        for y in range(tvy,tvy+tvheight):
            print('')
            for x in range(tvx,tvx+tvwidth):
                r = output.array[y,x,0] *3
                g = output.array[y,x,1]*3
                b = output.array[y,x,2]*3
                if  y>tvy and y < tvy+tvheight  and x>tvx and x<tvx+tvwidth:
                   print(color('___','white',(r,g,b)),end='')
                   red=red+r
                   green=green+g
                   blue=blue+b
                else:
#                   print(color('   ','white',(r,g,b)),end='')
                   pass
print("")

pixcount = tvwidth*tvheight
red=red/pixcount
green=green/pixcount
blue=blue/pixcount

print(red,green,blue)
print(color('                   ','white',(red*3,green*3,blue*3)))
print(color('                   ','white',(red*3,green*3,blue*3)))
print(color('                   ','white',(red*3,green*3,blue*3)))
print(color('                   ','white',(red*3,green*3,blue*3)))
c = Color(rgb=(float(red)/255,float(green)/255,float(blue)/255))
hue=int(c.hue *65535)
sat=int(c.saturation *255)
lum=int(c.luminance *255)
print(hue,sat,lum)

myHue.setHue('8', hue)
myHue.setSaturation('8', sat)
myHue.setBrightness('8', lum)
