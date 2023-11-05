With a Raspberry Pi Pico at hand it is pretty easy to dump the chip that holds
the BIOS password of a Thinkpad T40 or similar.

Attach wires, start laptop, start Raspberry Pi Pico and dump the chip. Then
use IBMpass from https://www.allservice.ro/ to descramble the password within
the dump.

My solution uses the MicroPython interactive environment. It's fun!
https://micropython.org/download/?port=rp2

The only annoying aspect is to attach cables to the chip. I used some of these
tiny hooks for IC legs. Others might solder some temporary wires or have
another person holding jumper wire pins in place.
