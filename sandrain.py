from mcpi import minecraft
from mcpi import block
from random import randint
import time

mc = minecraft.Minecraft.create ()

delay = 0.1

while True:
    x, y, z = mc.player.getPos()
    rx, rz = randint(int(x-radius), int(x+radius)), randint(int(z-radius), int(z+radius))
    mc.setBlock(rx, 50, rz, block.SAND.id)
    time.sleep(delay)