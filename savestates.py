from mcpi import minecraft
from mcpi import block
from random import randint
import time

mc = minecraft.Minecraft.create ()

print("1: Make a save")
print("2: Load a save")
choice = int(input())

while True:
    if choice == 1:
        mc.saveCheckpoint() 
    if choice == 2:
        mc.restoreCheckpoint()