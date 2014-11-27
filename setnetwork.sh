#!/bin/bash
if [ $# = 2 ]; then
  ifconfig wlp0s29u1u7 down
  iw dev wlp0s29u1u7 set type ibss
  ifconfig wlp0s29u1u7 192.160.1.1 up
  iw dev wlp0s29u1u7 ibss join pyOSNet 2462
else
  echo "Por favor use setnetwork.sh deviceName IP"
fi