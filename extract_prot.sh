#!/bin/bash

# Loop through all the directories
for i in $(seq 0 99)
do
  printf -v j "%03d" $i
  dir=CLONE$j
  if [ -d "$dir" ]
  then
     cd $dir 
     # Loop through all the frames
     for k in $(seq 0 99)
     do 
         printf -v l "%03d" $k
         file=frame$l.xtc
         file2=frame$l-prot.xtc
         if [ -f "$file" ] && [ ! -f $file2 ]
         then
             echo $file
             gmx_mpi trjconv -f $file -s ../top.pdb -o $file2 < ../groups.txt &> $l.log
         fi
     done
     cd ../
  fi
done
