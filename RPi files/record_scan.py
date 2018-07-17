#!/usr/bin/env python3

from sweeppy import Sweep
import math
import os

with Sweep('/dev/ttyUSB0') as sweep:
    speed = sweep.get_motor_speed()
    rate = sweep.get_sample_rate()

    print('Motor Speed: {} Hz'.format(speed))
    print('Sample Rate: {} Hz'.format(rate))
    i = 0
    while os.path.exists("/home/pi/lidarData/sweep%s.csv" % i):
        i += 1
    datafile = open("/home/pi/lidarData/sweep%s.csv" % i, "w")
    datafile.write("angle, distance, x, y\n")
    sweep.start_scanning()
    maxscan = 5
    scancount = 0
    for scan in sweep.get_scans():
        print('{}\n'.format(scan))
        scancount = scancount + 1
        if scancount == maxscan:
            for samp in scan.samples:
                print(samp)
                print("angle (deg), distance (cm), x, y\n")
                degrees = samp.angle / 1000.0
                x = samp.distance * math.cos(degrees * math.pi / 180)
                y = samp.distance * math.sin(degrees * math.pi / 180)
                print("%f, %f, %f, %f\n" % (degrees, samp.distance, x, y))
                datafile.write("{0}, {1}, {2}, {3}\n".format(degrees, samp.distance, x, y))
                print(degrees, samp.distance, x, y)
                print("{0}, {1}, {2}, {3}\n".format(degrees, samp.distance, x, y))
            break
datafile.close()
    
