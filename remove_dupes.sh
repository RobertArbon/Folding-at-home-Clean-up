#!/bin/bash

for i in $(seq 0 45)
do
  printf -v j "%03d" $i
  dir1=CLONE$j
  file1=clone$j.xtc
  if [ -d "$dir1" ]
  then
   echo "Cleaning $dir1.xtc"
   python remove_dupes.py $dir1  
  fi
done
