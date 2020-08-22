#!/bin/bash

if [ ! -f "micropython-tm1637/tm1637.py" ];
then
    git clone https://github.com/mcauser/micropython-max7219
fi

ampy -p /dev/ttyUSB0 put micropython-tm1637/tm1637.py
ampy -p /dev/ttyUSB0 put main.py