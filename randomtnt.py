from mcpi import minecraft
from mcpi import block
from random import randint
import time

mc = minecraft.Minecraft.create ()
radius = 10
delay = 0.5
blockChoice = block.TNT.id

mc.postToChat("MWHAHAHA")
mc.postToChat("Escape the TNT!")

while True:
    x, y, z = mc.player.getPos()
    rx, rz = randint(int(x-radius), int(x+radius)), randint(int(z-radius), int(z+radius))
    dy = mc.getHeight(rx, rz)
    mc.setBlock(rx, dy, rz, blockChoice, 1)
    time.sleep(delay)