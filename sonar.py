#!/usr/bin/python
import time
import RPi.GPIO as GPIO

GPIO_TRIGGER = 23
GPIO_ECHO = 24

class Sonar:
  def __init__(self, trigPin = GPIO_TRIGGER, echoPin = GPIO_ECHO):

    GPIO.setmode(GPIO.BCM)
    self.mTriggerPin = trigPin
    self.mEchoPin = echoPin

    GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
    GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

    GPIO.output(GPIO_TRIGGER, False)

  def readContinuous(self):
    
    while True:
      time.sleep(0.1)
      value = self.readValue()
      print value

  def readValue(self):
    
    # Send 10us pulse to trigger
    GPIO.output(self.mTriggerPin, True)
    time.sleep(0.00001)
    GPIO.output(self.mTriggerPin, False)
    start = time.time()
  
    while GPIO.input(self.mEchoPin)==0:
      start = time.time()
        
    while GPIO.input(self.mEchoPin)==1:
      stop = time.time()

    # Calculate pulse length
    elapsed = stop-start
  
    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000

    # That was the distance there and back so halve the value
    distance = distance / 2

    return distance

  def cleanup(self):
    GPIO.cleanup()

