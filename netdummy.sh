#!/bin/bash
if [ $# = 2 ]; then
  echo 'configuring ' , $1
  echo 'setting ', $1 , 'in adhoc mode'
  echo 'connecting up to IP ' , $2
else
  echo "Por favor use netdummy.sh deviceName IP"
fi