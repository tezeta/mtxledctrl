#!/usr/bin/env python3
#mtxledctrl 1.1
#tezeta 2021

import ctypes, time, telnetlib

c_uint8 = ctypes.c_uint8

#led status is controlled via bitmask
#six GPO bits control the LEDS
#more info in Matrix Orbital's documentation

class GPIO_bits( ctypes.LittleEndianStructure ):
    _fields_ = [
                ("a", c_uint8, 1 ),
                ("b", c_uint8, 1 ),
                ("c", c_uint8, 1 ),
                ("d", c_uint8, 1 ),
                ("e", c_uint8, 1 ),
                ("f", c_uint8, 1 ),
               ]

class GPIO( ctypes.Union ):
    _anonymous_ = ("bit",)
    _fields_ = [
                ("bit",    GPIO_bits ),
                ("asByte", c_uint8    )
               ]

gpio = GPIO()
gpio.asByte = 0x0

class mtxledctrl:
    def __init__(self, ip, port, dbg):
        self.dbg = dbg

        try:
            self.tn = self.debug(telnetlib.Telnet(ip, port))
            self.tn.write(b"hello\n")
            self.debug(self.tn.read_until(b'\n'))
        except ConnectionRefusedError:
            error("Failed to connect to server!")
            exit(1)

        for colortest in ['r','o','g','']:
            for ledtest in ['1','2','3']:
                self.debug("testing led " + ledtest)
                self.queuecolor(ledtest, colortest)
            self.sendcmd()
            time.sleep(0.5)

    def debug(self, message):
        if self.dbg:
            print("debug: " + str(message))
        return message

    def error(self, message):
        print("ERROR: " + str(message))
        return message

    def sendcmd(self):
        byte = str(gpio.asByte) # get bitmask as number
        string = "output " + str(gpio.asByte) + "\n"
        self.debug("send command \"" + string.rstrip() + "\"")
        self.tn.write(string.encode('utf-8'))
        self.debug("recieved \"" + str(self.tn.read_until(b"\n")) + "\"")

    def queuecolor(self, led, color):
        #led logic based on MXO's documentation
        #if the color is not defined assume it should be off
        led = int(led)
        if led==1:
            gpio.a=0
            gpio.b=0
            if color=='r':
                gpio.a=1
                gpio.b=0
            if color=='g':
                gpio.a=0
                gpio.b=1
            if color=='o':
                gpio.a=1
                gpio.b=1
        if led==2:
            gpio.c=0
            gpio.d=0
            if color=='r':
                gpio.c=1
                gpio.d=0
            if color=='g':
                gpio.c=0
                gpio.d=1
            if color=='o':
                gpio.c=1
                gpio.d=1
        if led==3:
            gpio.e=0
            gpio.f=0
            if color=='r':
                gpio.e=1
                gpio.f=0
            if color=='g':
                gpio.e=0
                gpio.f=1
            if color=='o':
                gpio.e=1
                gpio.f=1
