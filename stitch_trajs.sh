#!/bin/bash

for i in $(seq 0 99)
do
  printf -v j "%03d" $i
  dir=CLONE$j
  if [ -d "$dir" ]
  then
    cd $dir
    file=clone$j.xtc
    if [ ! -f $file ]
    then 
        gmx_mpi trjcat -cat -f frame*-prot.xtc -o $file &> clone$j.log 
        echo "Created $file"
    else
        echo "$file already exists"
    fi
    cd ../
  fi
done
