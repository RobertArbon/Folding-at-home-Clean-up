#!/bin/bash

#maxframe=0
#for i in {0..200}
#do
#    fname=CLONE1/frame"$i".xtc
#    echo $fname
#    if [ ! -f $fname ]
#    then
#       maxframe="$i"
#       break
#    fi
#done
for i in $(seq 0 99)
do
  printf -v j "%03d" $i
  dir1=CLONE$i
  if [ -d "$dir1" ]
  then
   mv $dir1 CLONE$j
  fi
done
