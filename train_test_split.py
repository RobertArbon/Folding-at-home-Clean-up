import mdtraj as md
import numpy as np
from os.path import join

np.random.seed(42)

# Save only trajectories longer than 501ns
# Timestep is 50ps = 0.05ns 
stride=40
ts=2
max_t = 501 # Need > 500 for TICA lag times 
ignore = 100 # Ignore this many ns of trajectory 
train_split=0.75

lengths=[]
trajs=[]
dirs = ['RUN{}'.format(i) for i in range(10)]
for dir in dirs: 
    for i in range(100):
        try:
           traj= md.load(join(dir, 'clone{:03d}-clean.xtc'.format(i)), top='top_prot.pdb', stride=stride)
           print('traj RUN{2}/{0} is {1} ns long'.format(i, traj.n_frames*ts, dir))
           if traj.n_frames*ts > max_t + ignore:
               print('\tadding traj RUN{0}/{1} to list, removing first {2} frames / {3} ns from beginning'.format(dir, i, ignore/ts, ignore))
               print('\told length {}'.format(traj.n_frames*ts))
               traj = traj[int(ignore/ts):]
               print('\tnew length {}'.format(traj.n_frames*ts))
               trajs.append(traj)
               lengths.append(traj.n_frames*ts)           
        except IOError:
            print('No trajectory {0}/{1}'.format(dir,i))

lengths = np.array(lengths)
indices = np.arange(len(lengths))

rand_idx = np.random.permutation(indices)
rand_lens = lengths[rand_idx] 
cum_rand_lens = np.cumsum(rand_lens)
print('-----------------------')
print('lengths           :\n', lengths)
print('random lengths    :\n', rand_lens)
print('cum random lengths:\n', cum_rand_lens)

train_len = train_split*cum_rand_lens[-1]
for i, len in enumerate(cum_rand_lens): 
    if len > train_len:
        idx=i
        break

train_idx = rand_idx[:idx]
test_idx = rand_idx[idx:]
print('Random Index:\n', idx)
print('Train indices:\n', train_idx)
print('Test indices:\n', test_idx)

print('Total test trajectories %   : {:4.2f}'.format(100*np.sum(rand_lens[test_idx])/np.sum(rand_lens)))
print('Total train trajectories %  : {:4.2f}'.format(100*np.sum(rand_lens[train_idx])/np.sum(rand_lens)))
print('Total test trajectories ns  : {:4.2f}'.format(np.sum(rand_lens[test_idx])))
print('Total train trajectories ns : {:4.2f}'.format(np.sum(rand_lens[train_idx])))
print('Total length trajectories ns: {:4.2f}'.format(np.sum(rand_lens)))

for idx in test_idx:
    trajs[idx].save('test/trajectory-{}.xtc'.format(idx))
for idx in train_idx:
    trajs[idx].save('train/trajectory-{}.xtc'.format(idx))
    

     
