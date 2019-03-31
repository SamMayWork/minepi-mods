from mcpi import minecraft
from mcpi import block
from random import randint
import time

mc = minecraft.Minecraft.create ()

cloudPositions = []
worldSize = 128

while True:
    rx, rz = randint(-worldSize, worldSize), randint(-worldSize, worldSize)
    for position in cloudPositions:
        if position[0] == rx and position[1] == rz:
            continue
    mc.setBlock(rx, 50, rz, block.WOOL.id)
    mc.setBlock(rx+1, 50, rz, block.WOOL.id)
    mc.setBlock(rx-1, 50, rz, block.WOOL.id)
    mc.setBlock(rx, 50, rz+1, block.WOOL.id)
    mc.setBlock(rx, 50, rz-1, block.WOOL.id)
    cloudPositions.append([rx, rz])
