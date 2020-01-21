#global vars are represented as all caps in python
#tell how big the tiles are
#dimensions of tiles in terms of pixels. 
TILESIZE = 48 #per pixel
GRIDWIDTH = 28
GRIDHEIGHT = 15
#can change these ^ tomorrow maybe.

GRIDWIDTH_PX = GRIDWIDTH * TILESIZE
GRIDHEIGHT_PX = GRIDHEIGHT * TILESIZE

FPS = 60 #frames per second, locked here. #refresh rate

#colours #py game knows these are colour codes... you can also use hex codes
WHITE = (255, 255, 255)
BLACK  = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255,  0)

#grey
LIGHT_GRAY = (40, 40, 40)
DARK_GRAY = (140, 140, 140)
