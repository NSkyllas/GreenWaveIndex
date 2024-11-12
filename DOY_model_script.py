import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import streamlit as st


dsh = xr.open_dataset('doy_mod_hist.nc')
dsn1 = xr.open_dataset('doy_mod_ssp126_nf.nc')
dsf1 = xr.open_dataset('doy_mod_ssp126_ff.nc')
dsn2 = xr.open_dataset('doy_mod_ssp245_nf.nc')
dsf2 = xr.open_dataset('doy_mod_ssp245_ff.nc')
dsn5 = xr.open_dataset('doy_mod_ssp585_nf.nc')
dsf5 = xr.open_dataset('doy_mod_ssp585_ff.nc')

for f in ['dsn5', 'dsf5', 'dsn2', 'dsf2', 'dsn1', 'dsf1', 'dsh', 'dss']:
    exec(f"{f}['doy'] = {f}['__xarray_dataarray_variable__']")
    exec(f"{f} = {f}.drop(['__xarray_dataarray_variable__'])")

weights = np.cos(np.deg2rad(dss.lat))
weights.name = "weights"

#fig, ax = plt.subplots(ncols = 5, nrows = 2, figsize = (20, 6), subplot_kw={'projection': ccrs.NorthPolarStereo()})
#ax = ax.flatten()
#for i, m in enumerate(model_list):
#    dsh.doy.sel(model = m).mean(['time']).plot(ax = ax[i], vmin = 100, vmax = 210, transform = ccrs.PlateCarree())
#    ax[i].coastlines()
#    ax[i].set_title(m)
#plt.suptitle('Historical, mean of 2000 - 2013', fontsize = 16)

fig, ax = plt.subplots(ncols = 5, nrows = 2, figsize = (20, 6))
ax = ax.flatten()
for i, m in enumerate(model_list):
    dsh.doy.sel(model = m).mean(['time']).plot(ax = ax[i], vmin = 100, vmax = 210)
plt.suptitle('Historical, mean of 2000 - 2013', fontsize = 16)

st.pyplot(fig)
