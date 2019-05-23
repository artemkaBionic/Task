#!/usr/bin/python3
import sys
import psutil
if sys.argv[1] == "cpu":
 print("system.cpu.idle " +str( psutil.cpu_times().idle))
 print("system.cpu.user "  + str(psutil.cpu_times().user))
 print("system.cpu.guest " + str(psutil.cpu_times().guest))
 print("system.cpu.iowait " + str(psutil.cpu_times().iowait))
 print("system.cpu.stolen " + str(psutil.cpu_times().steal))
 print("system.cpu.system " + str(psutil.cpu_times().system))
elif sys.argv[1] == "mem":
 print("virtual total " + str(psutil.virtual_memory().total))
 print("virtual used " + str(psutil.virtual_memory().used))
 print("virtual free " + str(psutil.virtual_memory().available))
 print("virtual shared " + str(psutil.virtual_memory().shared))
 print("swap total " + str(psutil.swap_memory().total))
 print("swap used " + str(psutil.swap_memory().used))
 print("swap free " + str(psutil.swap_memory().free))
else:
 print("Please input correct param! mem or cpu to get relate info")

