# Import all of the minecraft tools that we need the make the mod!
from mcpi import minecraft
from mcpi import block
from random import randint
import time

# Attach the mod to the game!
mc = minecraft.Minecraft.create ()

# The minimum level we're going to start generating water at
floor = 1

# The square size of the world
worldSize = 26

# A fancy way of saying "forever"
while True:

    # This section looks a little complicated but I promise it's
    # simpler than it looks - essentially what we're doing is checking
    # to see if every block in the world is air, if it is we're going to
    # to turn it into water, otherwise we're going to leave it.

    # All of the blocks in the world are arranged into a grid with rows
    # and columns, what the code below does is go through every column in
    # every row - if you don't unserstand how this works, ask one your volunteers!
    for x in range (-worldSize, worldSize):
        for z in range (-worldSize, worldSize):

            # Is the block empty?
            if mc.getBlock(x, floor, z) == block.AIR.id:
                # Turn it into water
                mc.setBlock(x, floor, z, block.WATER.id)

    # Once this entire level has been converted into water, start
    # on the level of blocks above
    floor += 1


# EXTENSION

# There's no delay in this program so why does it take so long to fill the world up with water?
# What happens if you change the size of thr world variable?
# What other blocks could you fill the world ip with?