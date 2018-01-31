#Christo
#1/31/18
#coloredSquare.py

from ggame import *
from random import randint

red = 1
blue = 2
green = 3 
yellow = 4

num = randint(1,4)

if num == 1:
    print(red = Color(0xff0000,1))
    line = LineStyle(3,red)
    rectangle1 = RectangleAsset(100,100,line,red)

    Sprite(rectangle1)
    myApp = App()
    myApp.run()
elif num ==2:
    print(blue = Color(0x0000ff,1))
    line = LineStyle(3,blue)
    rectangle2 = RectangleAsset(100,100,line,blue)

    Sprite(rectangle2)
    myApp = App()
    myApp.run()

green = Color(0x00cc00,1)
line = LineStyle(3,green)
rectangle3 = RectangleAsset(100,100,line,green)

Sprite(rectangle3)
myApp = App()
myApp.run()

yellow = Color(0xffff00,1)
line = LineStyle(3,yellow)
rectangle4 = RectangleAsset(100,100,line,yellow)

Sprite(rectangle4)
myApp = App()
myApp.run()