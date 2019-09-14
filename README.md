# waterbot
code for controlling a Raspberry-Pi-controlled boat

Starting with a Raspberry Pi with a camera and a pan/tilt mechanism (see 
https://learn.sparkfun.com/tutorials/setting-up-the-pi-zero-wireless-pan-tilt-camera/all )

I added an L293D dual H-bridge controlling a reversible propulsion motor and a rudder toggle (electrically identical to a reversible motor) for a small plastic boat, which the Rasperry Pi 
could then control.  I added buttons to the pan/tilt camera control page to control the propulsion and steering of the boat,
making the basis for a "first person" remote piloted watercraft.   

The code for all this ends up in the root of /var/www/[whatever location your pan/tilt camera ended up in, often 'html'].

To do:  make the rudder and propulsion systems proportional with slider UI interfaces and PWM.


NOTES:  Is this right?:
https://robotics.stackexchange.com/questions/9048/l293d-wont-turn-motor-backwards
"The motor driver chip you state you are using, the L293D, is a "quadruple half H driver." This means that, instead of two full H circuits capable of driving a motor forward and reverse, you have four half H circuits, which are only capable of driving a motor in one direction."

I'm pretty sure now that that commentator was wrong. My symptoms at the wires going to the motor is that when the H-bridge is is one direction, the voltage is -12 volts and in the other direction the voltage is 3 volts.  Perhaps the motor is drawing too much current?

I measured the voltages coming off the L293D with no load and it was 9volts in one direction and 9volts in the other.  So perhaps the rudder system in the boat I am using is inherently incompatible with the L293D.

I treied the L293D with an electric motor instead of the rudder on the toy boat I'd been using. It was able to rotate the motor both directions, but it went much faster in one direction than the other.
