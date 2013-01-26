#!/usr/bin/python2.7

import pygame.mixer
from time import sleep
from sys import exit
from os import listdir

def getSoundFiles():
    return listdir("sounds/")

if __name__ == "__main__":

    print("[+] Initializing pygame mixer");
    pygame.mixer.init(44000, -16, 1, 1024)
    
    print("[+] Initalizing sounds from \"sound/\" folder")
    sounds = []
    for f in getSoundFiles():
        sounds.append(pygame.mixer.Sound("sounds/" + f))
                     
    soundChannel = pygame.mixer.Channel(1)

    soundCounter = 0
    while 1:
        print("[+] Playing sound " + str(soundCounter))
        soundChannel.play(sounds[soundCounter])
        sleep(5)

        soundCounter += 1
        if soundCounter >= len(sounds):
            soundCounter = 0






