#!/bin/bash
#PBS -S /bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=02:00:00
#PBS -N VillinData 
#PBS -V


cd $PBS_O_WORKDIR
source activate ml4dyn
bash rename_dirs.sh
bash rename_files.sh
bash extract_prot.sh
bash stitch_trajs.sh
bash remove_dupes.sh
