import pyphue
from colour import Color
myHue = pyphue.PyPHue(ip='192.168.0.157',user='DuuwppZiNJCneZcgQQs-01ckob4yjYnHw0UmoM0V')
print(myHue.lightIDs)
c = Color(rgb=(0.11,0.1,0.8))
hue=int(c.hue *255)
sat=int(c.saturation *255)
lum=int(c.luminance *255) 
print(hue,sat,lum)

myHue.setHue('8', hue)  
myHue.setSaturation('8', sat)  
myHue.setBrightness('8', lum)  


