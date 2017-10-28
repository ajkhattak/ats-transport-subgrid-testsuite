import numpy as np
import h5py
d = h5py.File("checkpoint00001.h5",'r')
d1 = h5py.File("visdump_data.h5",'r')
d2 = h5py.File("ss_flow_results.h5",'w')
d2.create_dataset("time", data=np.array([0.,]))
flux = d2.create_group("mass_flux.face.0")
pd = d2.create_group("saturation_liquid.cell.0")
flux.create_dataset("0", data=d['mass_flux.face.0'][:])
pd.create_dataset("0", data=d1['saturation_liquid.cell.0']['1'][:])

d.close()
d2.close()
