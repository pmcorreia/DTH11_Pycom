#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

# See https://docs.pycom.io for more information regarding library specifics

import gc
import time

import _thread
import pycom
from _pybytes import Pybytes
from dth import DTH
from machine import Pin

pycom.heartbeat(False)
pycom.rgbled(0x000008) # blue
th = DTH(Pin('P3', mode=Pin.OPEN_DRAIN),0)
time.sleep(2)




def send_env_data():
        
        while (pybytes):
                pycom.rgbled(0x7f0000) # red
                result = th.read()
                temperature = int(result.temperature)
                humidity = int(result.humidity)
                if result.is_valid():
                        pycom.rgbled(0x001000) # green
                        pybytes.send_signal(2, temperature)
                        pybytes.send_signal(1, humidity)
                        time.sleep(10)
                gc.collect()
_thread.start_new_thread(send_env_data, ())
