import mdtraj as md
import numpy as np
import sys
from os.path import join, isfile

if len(sys.argv) != 2:
    sys.exit(1)

dir_name = sys.argv[1]
oldfname = join(dir_name.upper(), '{}.xtc'.format(dir_name.lower()))
newfname = join(dir_name.upper(), '{}-clean.xtc'.format(dir_name.lower()))
print('\tChecking for {0} and {1}'.format(oldfname, newfname))

if isfile(oldfname) and not isfile(newfname):

    traj = md.load(join(dir_name.upper(), '{}.xtc'.format(dir_name.lower())), top='top_prot.pdb')
    keep = list(range(traj.n_frames))
    duplicates = []
    
    # Remove all the duplicate frames that aren't the start of each frame
    idx = traj.n_frames-1
    jdx = 1
    ts = traj.time
    while jdx >= 0: 
        if ts[idx] != 0:
            jdx = idx-1
            while ts[jdx] >= ts[idx]:
                keep.remove(jdx)
                duplicates.append(jdx)
                jdx -= 1
            idx = jdx
        idx -=1
    
    
    # No remove all frames with timestamp zero, except the first one: 
    zeros = np.where(traj.time==0.)[0][1:]
    keep = [x for x in keep if x not in zeros]
    
    traj2 = traj[keep]
    
    print('\toriginal length: {:>8}'.format(traj.n_frames))
    print('\tnum duplicates:  {:>8}'.format(len(duplicates)))
    print('\tnum zeros:       {:>8}'.format(len(zeros)))
    print('\tnew length:      {:>8}'.format(traj2.n_frames))
    
    # Print out length in ns 
    dt = np.round(traj2.timestep)/1000.
    print('\tnew length (ns):  {:>8.2f}'.format(dt*traj2.n_frames))
    
    # Save trajectory
    if traj.n_frames == (len(duplicates) + traj2.n_frames+len(zeros)):
        traj2.save(join(dir_name.upper(), '{}-clean.xtc'.format(dir_name.lower())))
        sys.exit(0)
    else:
        print('Error!')
        sys.exit(1)
else:

    print('\tEither {0} missing or {1} already there'.format(oldfname, newfname))
