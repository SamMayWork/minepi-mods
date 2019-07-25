# Import all of the minecraft tools that we need the make the mod!
from mcpi import minecraft
from mcpi import block
from random import randint
import time

# Attach the mod to the game!
mc = minecraft.Minecraft.create ()

# An option that prints the location of each tower in the chat!
talkLoads = False

# The square size of the world
worldSize = 128

# The maximum height of the towers
towerHeight = 100

# The block we're going to use to make the towers!
blockChoice = block.STONE.id

# A fancy way of saying "forever"
while True:

    # Pick a random block to make the tower at
    rx, ry = randint(-worldSize, worldSize), randint(-worldSize, worldSize)

    # If we're supposed to be talking loads print the location of the tower
    if talkLoads == True:
        mc.postToChat("Placing tower @ ", rx, ry)

    # Start at the bottom of the tower and add a block all the way up the tower
    for y in range (0, towerHeight):
        mc.setBlock (rx, y, ry, blockChoice)

# EXTENSION

# What happens if you change the height of the towers?
# How would you change the material the torwer is made of?
# What would be the effect of changing line 33 to "for y in range (0, towerHeight, 2):" (put it in your code and try it out!)
# What happens if you change the variable for the world size?
# How could you improve this code? 