#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pyfprint

pyfprint.fp_init()
devs = pyfprint.discover_devices()
dev = devs[0]
dev.open()
fprint = dev.load_print_from_disk(pyfprint.Fingers['RIGHT_INDEX'])

verified, img = dev.verify_finger(fprint)

if verified:
    print("MATCH!")
else:
    print("NO MATCH!")
if img is not None:
    img.save_to_file('verify.pgm')
    print("Wrote scanned image to verify.pgm")
dev.close()
pyfprint.fp_exit()
