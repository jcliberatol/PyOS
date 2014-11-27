#!/usr/bin/env python
import os
SOROOT = "/home/SOROOT"
if not os.path.isdir(SOROOT):
  os.makedirs(SOROOT)
  print("Nuevo servidor en  : ",SOROOT)
  
