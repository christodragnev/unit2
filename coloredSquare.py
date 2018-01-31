#Christo
#1/31/18
#coloredSquare.py

from ggame import *

red = Color(0xff0000,1)
line = LineStyle(3,red)
rectangle1 = RectangleAsset(100,100,line,red)

Sprite(rectangle1)
myApp = App()
myApp.run()


blue = Color(0x0000ff,1)
line = LineStyle(3,blue)
rectangle2 = RectangleAsset(100,100,line,blue)

Sprite(rectangle2)
myApp = App()
myApp.run()