#rover

code for controlling a Raspberry-Pi-controlled rover, which is just a large remote-controlled toy vehicle with its R/C electronics replaced by a Raspberry Pi and motor drivers.

Starting with a Raspberry Pi with a camera and a pan/tilt mechanism (see https://learn.sparkfun.com/tutorials/setting-up-the-pi-zero-wireless-pan-tilt-camera/all )

I added an L298N dual H-bridge controlling a reversible drive motor and another motor that drives a rack & pinion steering rig. The drive motor is controlled by Raspbery Pi GPIO pin #18 and pins #20 and #21. The steering is controlled by GPIO pins #24, #19, and #16.

The code for all this ends up in the root of /var/www/[whatever location your pan/tilt camera ended up in, often 'html'].
