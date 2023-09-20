# adjust pin numbers,
# copy this file to /pyboard/main.py and start playing.
# get the dump from /pyboard/dump
# I'm using rshell for this

from machine import I2C, Pin
import time

devaddr_normal = 0x54
devaddr_extra  = 0x5c

BLOCKS   = 8
PAGES    = 8
PAGESIZE = 16 # bytes

def scan_hex():
    return [hex(x) for x in i2c.scan()]

prot_n = Pin(6,  Pin.OUT, value=1)
wp     = Pin(28, Pin.OUT, value=1)
i2c    = I2C(1, freq=40000, scl=Pin(27), sda=Pin(26))

def dump():
    with open('dump', 'wb') as f:
        for block in range(BLOCKS):
            for page in range(PAGES):
                addr = (block&1)*PAGES*PAGESIZE + page*PAGESIZE
                print(f"Sequentially reading {PAGESIZE} bytes from block {block}, page {page} -> addr {addr}")
                devaddr = devaddr_normal + (block>>1)
                print(f"The device address is {hex(devaddr)}")
                f.write(i2c.readfrom_mem(devaddr, addr, PAGESIZE))

# just dump the APP bytes for the protection of the main 8 blocks of memory
# APP page at memory addresses 0x00 to 0x0f
# ID  page at memory addresses 0x10 to 0x1f
def dump_app():
    for i in range(8):
        val = i2c.readfrom_mem(devaddr_extra, i, 1)
        print(f"APP byte {i}: {val}")

# a: first block to unlock
# b: last block to unlock + 1 
# example: unlock(1, 2) to only unlock block 1
def unlock(a, b):
    wp.value(0)
    for i in range(a,b):
        wbuf = bytearray([0xff])
        i2c.writeto_mem(devaddr_extra, i, wbuf)
        time.sleep_ms(500)
        val = i2c.readfrom_mem(devaddr_extra, i, 1)
        print(f"APP byte {i}: {val}")
    wp.value(1)
