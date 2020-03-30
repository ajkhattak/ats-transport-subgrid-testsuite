import h5py
import numpy as np

d=h5py.File("flow/checkpoint_final.h5",'r')
d1=h5py.File("faceQ.h5",'w')

#rho_m = 55555.*0.1
rho_m = 0.1
dx = np.where(d["surface-mass_flux.face.0"][:] >0, rho_m, -rho_m)

print (len(dx))
for i,x in enumerate(d["surface-mass_flux.face.0"][:]):
    if x == 0:        
        dx[i] = 0

#print (dx, d["surface-mass_flux.face.0"][:])

grp = d1.create_group('surface-mass_flux.face.0')
grp.create_dataset("0",data=dx)
d1.create_dataset("time",data=np.array(0))
d1.close()
d.close()
