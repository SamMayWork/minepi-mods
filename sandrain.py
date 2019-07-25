# Import all of the minecraft tools that we need the make the mod!
from mcpi import minecraft
from mcpi import block
from random import randint
import time

# Attach the mod to the game!
mc = minecraft.Minecraft.create ()


# First thing's first we need to pick the block we're going to drop
# on the player, for this example we're going use the sand!
fallingBlock = block.SAND.id

# The size of the circle around the player in which we can drop the
# block - it would get boring if we dropped a block on the players head
# every single time!
radius = 10

# The height to drop the block from!
dropHeight = 50

# The delay between "droplets" of blocks falling
delay = 0.1


if fallingBlock == block.SAND.id:
    mc.postToChat("A sand storm is approaching!")
if fallingBlock == block.GRAVEL.id:
    mc.postToChat("A gravel storm is approaching")
else:
    mc.postToChat("There is no storm approaching, but what's that in the sky!?")

# A fancy way of saying "forever"
while True:

    # Let's get the x, y, and z position of the player (ask if you're not sure what this means!)
    x, y, z = mc.player.getPos()

    # Now we need to pick a random block within the radius of that player
    # to drop the block on - to do this we're going the take the current position
    # of the player and pick somewhere within that radius
    rx, rz = randint(int(x-radius), int(x+radius)), randint(int(z-radius), int(z+radius))

    # Drop the block!
    mc.setBlock(rx, dropHeight, rz, fallingBlock)

    # Wait until we can send the next droplet!
    time.sleep(delay)


# Experiment!

# - What happens if you change the block?
#   - What happens if you change the block to Gravel?
#   - Why don't some blocks drop?
#   - What message appears in the chat if you don't pick either sand or gravel?
#
# - What happens if you change the drop height of the block?
# - What happens if you increase/decrease the radius variable?
# - What happens if you change the delay?
#   
# - What set of variables would cause the most chaos?