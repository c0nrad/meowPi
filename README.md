MeowPI
==========

![meowPi](https://github.com/c0nrad/meowPi/blob/master/images/meowPi.jpg?raw=true)

meowPi is a Raspberry Pi program that emits a meow when a trip wire is activated.



Introduction
-

Every person has a responsibility to himself and the world. As Gandhi once said: <i> "Whatever you do will be insignificant, but it is very important that you do it." </i> 

Unfortunetly Gandhi wasen't alive to see the creation of RPi meowers, but if he were alive today, I'm sure he'd change his quote to reflect the importantace of these devices.

Anyways, let's get started. 

Background Information
-

In this tutorial you'll be building a ultrasonic based tripwire for your Raspberry Pi that'll play a "meow" sound when activated. 
	  
Sonar works by emitting a pulse of sound, and timing how long it takes for that sound to to bounce back to a reciever. Since we know how fast sound travels (~340m/s) and we can figure out how long the sound took to get there and come back, we can calculate the distance of the object. 

![Sonar](https://github.com/c0nrad/meowPi/blob/master/images/sonarDiagram.png?raw=true)

To play sounds we'll be using the <i>pygame.mixer</i> library. This library should already be installed on your RPi assuming you're using wheezy. 

Parts 
-	  

* [Raspberry Pi](http://www.amazon.com/Raspberry-Pi-Model-Revision-512MB/dp/B009SQQF9C/ref=sr_1_1?ie=UTF8&qid=1362138473&sr=8-1&keywords=raspberry+pi)
* [Cobbler Breakout Kit](http://www.adafruit.com/products/914)
* [Breadboard](http://www.amazon.com/BB400-Solderless-Plug-BreadBoard-tie-points/dp/B0040Z1ERO/ref=pd_sim_e_3)
* [Ultrasonic Sonar (HC-SR04)](http://www.amazon.com/Ultrasonic-Module-HC-SR04-Distance-Arduino/dp/B004U8TOE6/ref=sr_1_1?ie=UTF8&qid=1362137669&sr=8-1&keywords=hc-sr04)
* [330 and 470 Ohm Resistors](http://www.amazon.com/Sparkfun-500-4W-Resistor-Kit/dp/B008MH97I4/ref=sr_1_1?s=electronics&ie=UTF8&qid=1362138498&sr=1-1&keywords=resistors)
* [Speakers with 3.5mm jack](http://www.amazon.com/Logitech-S120-2-0-Multimedia-Speakers/dp/B000R9AAJA/ref=sr_1_2?s=electronics&ie=UTF8&qid=1362138535&sr=1-2&keywords=speakers)

Hardware Setup 
-

First up we'll be wiring the sonar to the RPi as follows : 
![Wiring](https://github.com/c0nrad/meowPi/blob/master/images/ultraSonicWiring.png?raw=true)  
<i> Image courtesy of Matt Hawkins </i>	   

Software 
-	  

The software is split into 4 main files:

* [meowPi.py](https://github.com/c0nrad/meowPi/blob/master/meowPi.py): Top level file. Checks for difference in sonar distance. Emits a meow if within certain range.
* [meow.py](https://github.com/c0nrad/meowPi/blob/master/meow.py): Driver for playing meow sounds.
* [sonar.py](https://github.com/c0nrad/meowPi/blob/master/sonar.py): Driver for sonar.
* [debug.py](https://github.com/c0nrad/meowPi/blob/master/debug.py): Simple debug output
	  
To run the code, simply run the command in terminal:

```bash
python2.7 meowPi.py
```
	  
And when an object is within a certain distance of the sonar, a meow is played.

Enjoy!	  