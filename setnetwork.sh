#!/bin/bash
if [ $# = 2 ]; then
  ifconfig $1 down
  iw dev $1 set type ibss
  ifconfig $1 $2 up
  iw dev $1 ibss join pyOSNet 2462
else
  echo "Por favor use setnetwork.sh deviceName IP"
fi