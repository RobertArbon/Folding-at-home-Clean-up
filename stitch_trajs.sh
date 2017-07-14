#!/bin/bash

for i in $(seq 0 45)
do
  printf -v j "%03d" $i
  dir=CLONE$j
  if [ -d "$dir" ]
  then
    cd $dir
    gmx_mpi trjcat -cat -f frame*.xtc -o clone$j.xtc &> clone$j.log 
    echo "Created clone$j.xtc"
    cd ../
  fi
done