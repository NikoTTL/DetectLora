#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/niko/Bastille/gr-lora/lib
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/niko/Bastille/gr-lora/build/lib:$PATH
export LD_LIBRARY_PATH=/home/niko/Bastille/gr-lora/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-lora 
