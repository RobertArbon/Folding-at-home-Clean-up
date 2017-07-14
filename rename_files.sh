#!/bin/bash

for i in $(seq 0 99)
do
  printf -v j "%03d" $i
  dir1=CLONE$j
  cd $dir1
  
  maxframe=-1
  for i in {0..200}
  do
      fname=frame"$i".xtc
      if [ -f $fname ]
      then
         maxframe="$i"
      fi
      if [ ! -f $fname ]
      then
         break
      fi
  done
  lastframe=-1
  for i in {0..200}
  do 
      fname=frame"$i".xtc
      if [ -f $fname ]
      then
        lastframe="$i"
      fi 
  done 
  echo $maxframe, $lastframe
  if [ "$maxframe" !=  "$lastframe" ]
  then 
      echo Error!  Non-contiguous frames:
      echo $dir1 -- $maxframe -- $lastframe 
  elif [ "$maxframe" == "$lastframe" ]
  then  
    # should have made max in sequence to be maxframe
    for k in $( seq 0 $maxframe )
    do 
       printf -v l "%03d" $k
       mv frame"$k".xtc  frame"$l".xtc
    done  
  else 
      echo Error - comparisons failed
  fi 

  cd ../
done
