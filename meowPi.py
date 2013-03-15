#!/usr/bin/python2.7

from time import sleep
from sys import exit
from meow import Meow
from sonar import Sonar
from debug import *

if __name__ == "__main__":
    meow = Meow()
    sonar = Sonar()
    
    while 1:
        sleep(.1)
        
        distance = sonar.readValue()
        infoMessage("[+] distance: ", distance)

        if distance < 100:
            meow.playNextSound()
            sleep(3)
                





