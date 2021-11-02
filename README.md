# mtxledctrl
LED controller for Matrix Orbital LCDs through LCDd. Tested with the LK204-7T-1U, should work with similiar models with LEDs.
Each LED can be either red, orange or green. Color changes are queued before sending them:
```
>>> import mtxledctrl
>>> tn = mtxledctrl.init("127.0.0.1","13666")
>>> mtxledctrl.queuecolor(1,'r')
>>> mtxledctrl.queuecolor(2,'o')
>>> mtxledctrl.queuecolor(3,'g')
>>> mtxledctrl.sendcmd(tn)
```
Includes a demo (ledproc), this only monitors a file for changes (i.e. /proc/diskstats), intended for use with hard drive activity.
