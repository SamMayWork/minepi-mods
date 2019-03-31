from mcpi import minecraft
from mcpi import block
from random import randint
import time

mc = minecraft.Minecraft.create ()

floor = 1
worldSiz = 128

while True:
    for x in range (-128, 128):
        for z in range (-128, 128):
            if mc.getBlock(x, floor, z) == 0:
                mc.setBlock(x, floor, z, block.WATER.id)
    floor += 1