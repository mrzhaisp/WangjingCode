#coding=utf-8
import sys,time
for i in range(0,110,10):
    sys.stdout.write("▓▓▓"+" %"+str(i))
    sys.stdout.flush()
    time.sleep(0.5)
