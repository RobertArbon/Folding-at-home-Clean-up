#!/bin/bash

for i in $(seq 0 99)
do
  printf -v j "%03d" $i
  dir=CLONE$j
  if [ -d "$dir" ]
  then
   echo "Cleaning $dir.xtc"
   python remove_dupes.py $dir  
  fi
done
