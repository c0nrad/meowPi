#!/usr/bin/python2.7
import pygame.mixer
from time import sleep
from sys import exit
from os import listdir
from debug import *

class Meow:
    def __init__(self):
        goodMessage("Initializing meower")

        infoMessage("Starting pygame mixer")
        pygame.mixer.pre_init(frequency=22050, size=-16, channels=1, buffer=256) 
        pygame.mixer.init()

        infoMessage("Initalizing sounds from \"sound/\" folder")
        self.mSounds = []
        self.mSoundMap = dict()
        counter = 0
        for f in self.getSoundFiles():
            self.mSounds.append(pygame.mixer.Sound("sounds/" + f))
            self.mSoundMap[counter] = f
            counter += 1

        infoMessage("Creating sound channels")        
        self.mSoundChannels = []
        self.mSoundChannels.append(pygame.mixer.Channel(1))
        self.mSoundChannels.append(pygame.mixer.Channel(2))
        self.mSoundChannels.append(pygame.mixer.Channel(3))

        self.mSoundCounter = 0
        self.mChannelCounter = 0


    def getSoundFiles(self):
        return listdir("sounds/")

    def playNextSound(self):
        self.playSound(self.mSoundCounter)

        self.mSoundCounter += 1
        self.mSoundCounter %= len(self.mSounds)

    def playSound(self, index):
        infoMessage("Playing sound: ", self.mSoundMap[index], " on channel: ", self.mChannelCounter)
        self.mSoundChannels[self.mChannelCounter].stop()
        self.mSoundChannels[self.mChannelCounter].play(self.mSounds[index])

        self.mChannelCounter += 1
        self.mChannelCounter %= len(self.mSoundChannels)

if __name__ == "__main__":

    m = Meow()
    
    while True:
        m.playNextSound()
        sleep(5)
