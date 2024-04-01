# -*- coding: utf-8 -*-
"""
This file allows for the running of TRAK in parallel. It can be called to run 
the chosen files with the desired number of parallel runs, it can also be 
told what TRAK command to run. 
"""
# imports
import subprocess
import os 
import time 
import sys

################################################################################################
# Supply the file list, the number of parallel runs, and the TRAK command to run
#(file_list, # parallel runs, command)

files = sys.argv[1]
parallel_runs = sys.argv[2]
command = sys.argv[3]

file_list = files.split(',')
int_parallel_runs = int(parallel_runs)

################################################################################################
# run the files
processes = set()

start = 0
for i in range(round((len(file_list) + 1)/int_parallel_runs)): 
    for k in range(start, start + int_parallel_runs): 
        try:
            p1 = subprocess.Popen([command, file_list[k]])
            processes.add(p1)
            if k == (start + int_parallel_runs - 1): 
                p1.wait()
            ## Condition that if you're at the end of the file list, wait here too 
            if k == len(file_list) - 1:
                p1.wait()
        except: 
            break 
    print('Successfully ran %s %s - Starting next processes' %(command, file_list[k]))
    start += int_parallel_runs
print('Parallel runs complete!')
################################################################################################
        