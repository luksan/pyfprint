#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pyfprint

pyfprint.fp_init()
devs = pyfprint.discover_devices()
dev = devs[0]
dev.open()
if dev.supports_imaging():
    img = dev.capture_image(True)
    img.save_to_file('finger.pgm')
    img.standardize()
    img.save_to_file('finger_standardized.pgm')
else:
    print("this device does not have imaging capabilities.")
dev.close()

pyfprint.fp_exit()
