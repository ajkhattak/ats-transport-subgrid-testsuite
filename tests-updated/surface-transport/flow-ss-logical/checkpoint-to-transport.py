import h5py
import numpy as np
m_rho = 55000./55000.

d = h5py.File("checkpoint00025.h5",'r')
#d = h5py.File("checkpoint01448.h5",'r')
d2 = h5py.File("ss_flow_results.h5",'w')
d2.create_dataset("time", data=np.array([0.,]))
flux = d2.create_group("surface-mass_flux.face.0")
pd = d2.create_group("surface-ponded_depth.cell.0")

mass_flux = d['surface-mass_flux.face.0'][:]*m_rho
Lx = len(mass_flux)
#print Lx
#m = 0.08*6.87*0.183
"""
for i in range(len(mass_flux)):
        #print mass_flux[i],i
	if mass_flux[i] > 4:
		mass_flux[i] = 0.2
	elif (mass_flux[i] < -4):
		mass_flux[i] = -.2
        elif (mass_flux[i] > 0):
		mass_flux[i] = 0.1
        else:
                mass_flux[i] = -0.1
"""
for i in range(len(mass_flux)):
	if (mass_flux[i] >0):
		mass_flux[i] = 0.1
	else:
		mass_flux[i] = -0.1

mass_flux = [round(x,10) for y in mass_flux for x in y]


print d['surface-mass_flux.face.0'][:-1], mass_flux


p_depth = d['surface-ponded_depth.cell.0'][:]

p_depth = [0.08,]*(Lx-1)
#print p_depth
flux.create_dataset("0",data=mass_flux)
pd.create_dataset("0",data=p_depth)

d.close()
d2.close()
