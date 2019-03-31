from mcpi import minecraft
from mcpi import block
from random import randint
import time

mc = minecraft.Minecraft.create ()
worldSize = 128
ceiling = 100
blockChoice = block.STONE.id

while True:
    rx, ry = randint(-worldSize, worldSize), randint(-worldSize, worldSize)
    mc.postToChat("Placing tower @ ", rx, ry)
    for y in range (ceiling, 0, -1):
        mc.setBlock (rx, y, rz, blockChoice.STONE.id)