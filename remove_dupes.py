import mdtraj as md
import sys
from os.path import join

if len(sys.argv) != 2:
    sys.exit(1)

dir_name = sys.argv[1]

traj = md.load(join(dir_name.upper(), '{}.xtc'.format(dir_name.lower())), top='top.pdb')

dupes = []
for i in range(traj.n_frames-1):
    t0 = traj.time[i]
    t1 = traj.time[i+1]
    if (abs(t0-t1) < 1e-6) or (t1 < t0):
        dupes.append(i)

keep = [x for x in range(traj.n_frames) if x not in dupes]
traj2 = traj[keep]
print('\toriginal length: {}'.format(traj.n_frames))
print('\tnum duplicates:  {}'.format(len(dupes)))
print('\tnew length:      {}'.format(traj2.n_frames))
if traj.n_frames == (len(dupes) + traj2.n_frames):
    traj2.save(join(dir_name.upper(), '{}-clean.xtc'.format(dir_name.lower())))
    sys.exit(1)
else:
    print('Error!')


