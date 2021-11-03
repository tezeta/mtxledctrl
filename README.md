# mtxledctrl
LED controller for Matrix Orbital LCDs through LCDd. Tested with the LK204-7T-1U, should work with similiar models with LEDs.
Each LED can be either red, orange or green. Color changes are queued before sending them:
```
>>> from mtxledctrl import mtxledctrl
>>> ledctrl = mtxledctrl("127.0.0.1","13666",True) #ip and port of LCDd server, debug messages
>>> ledctrl.queuecolor(1,'r')
>>> ledctrl.queuecolor(2,'o')
>>> ledctrl.queuecolor(3,'g')
>>> ledctrl.sendcmd()
```
Includes a demo (ledproc), this monitors /proc/diskstats and flashes LEDs based on drive activity. Use IDs found in /dev/disk/by-id and seperate them with |. Useful for showing activity for specific RAID arrays.
