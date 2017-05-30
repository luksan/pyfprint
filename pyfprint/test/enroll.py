#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pyfprint

pyfprint.fp_init()
devs = pyfprint.discover_devices()
dev = devs[0]
dev.open()
fprint, img = dev.enroll_finger()
if fprint is not None:
    fprint.save_to_disk(pyfprint.Fingers['RIGHT_INDEX'])
if img is not None:
    img.save_to_file('enrolled.pgm')
    print("Wrote scanned image to enrolled.pgm")
dev.close()
pyfprint.fp_exit()
