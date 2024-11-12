import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import streamlit as st

dsh = xr.open_dataset('doy_mod_hist.nc', engine = 'netcdf4')
dsn1 = xr.open_dataset('doy_mod_ssp126_nf.nc', engine = 'netcdf4')
dsf1 = xr.open_dataset('doy_mod_ssp126_ff.nc', engine = 'netcdf4')
dsn2 = xr.open_dataset('doy_mod_ssp245_nf.nc', engine = 'netcdf4')
dsf2 = xr.open_dataset('doy_mod_ssp245_ff.nc', engine = 'netcdf4')
dsn5 = xr.open_dataset('doy_mod_ssp585_nf.nc', engine = 'netcdf4')
dsf5 = xr.open_dataset('doy_mod_ssp585_ff.nc', engine = 'netcdf4')

for f in ['dsn5', 'dsf5', 'dsn2', 'dsf2', 'dsn1', 'dsf1', 'dsh']:
    exec(f"{f}['doy'] = {f}['__xarray_dataarray_variable__']")
    exec(f"{f} = {f}.drop(['__xarray_dataarray_variable__'])")

weights = np.cos(np.deg2rad(dsh.lat))
weights.name = "weights"

model_list = dsn2.model.values

#fig, ax = plt.subplots(ncols = 5, nrows = 2, figsize = (20, 6), subplot_kw={'projection': ccrs.NorthPolarStereo()})
#ax = ax.flatten()
#for i, m in enumerate(model_list):
#    dsh.doy.sel(model = m).mean(['time']).plot(ax = ax[i], vmin = 100, vmax = 210, transform = ccrs.PlateCarree())
#    ax[i].coastlines()
#    ax[i].set_title(m)
#plt.suptitle('Historical, mean of 2000 - 2013', fontsize = 16)

scenario = st.sidebar.selectbox(
    'Pick a scenario',['No selection', 'historical', 'SSP-2.45', 'SSP-5.85'])
period = st.sidebar.selectbox('Pick a time period', ['No selection', 'Present', 'Near future (2040-2060)', 'Far future (2080-2100)'])
#season = st.sidebar.selectbox('Pick a season', ['No selection', 'Spring', 'Autumn'])

'You selected: ', scenario, period

if (scenario == 'historical') & (period == 'Present'):
    fig, ax = plt.subplots(ncols = 5, nrows = 2, figsize = (20, 6))
    ax = ax.flatten()
    for i, m in enumerate(model_list):
        dsh.doy.sel(model = m).mean(['time']).plot(ax = ax[i], vmin = 100, vmax = 210)
    plt.suptitle('Historical, mean of 2000 - 2013', fontsize = 16)
    plt.tight_layout()
    st.pyplot(fig)

elif (scenario == 'SSP-2.45') & (period == 'Near future (2040-2060)'):
    fig, ax = plt.subplots(ncols = 5, nrows = 2, figsize = (20, 6))
    ax = ax.flatten()
    for i, m in enumerate(model_list):
        dsn2.doy.sel(model = m).mean(['time']).plot(ax = ax[i], vmin = 100, vmax = 210)
    plt.suptitle('SSP-2.45, mean of 2040 - 2060 (near future)', fontsize = 16)
    plt.tight_layout()
    st.pyplot(fig)

elif (scenario == 'SSP-2.45') & (period == 'Far future (2080-2100)'):
    fig, ax = plt.subplots(ncols = 5, nrows = 2, figsize = (20, 6))
    ax = ax.flatten()
    for i, m in enumerate(model_list):
        dsn2.doy.sel(model = m).mean(['time']).plot(ax = ax[i], vmin = 100, vmax = 210)
    plt.suptitle('SSP-2.45, mean of 2040 - 2060 (far future)', fontsize = 16)
    plt.tight_layout()
    st.pyplot(fig)

elif (scenario == 'SSP-5.85') & (period == 'Near future (2040-2060)'):
    fig, ax = plt.subplots(ncols = 5, nrows = 2, figsize = (20, 6))
    ax = ax.flatten()
    for i, m in enumerate(model_list):
        dsn2.doy.sel(model = m).mean(['time']).plot(ax = ax[i], vmin = 100, vmax = 210)
    plt.suptitle('SSP-5.85, mean of 2040 - 2060 (near future)', fontsize = 16)
    plt.tight_layout()
    st.pyplot(fig)

elif (scenario == 'SSP-5.85') & (period == 'Far future (2080-2100)'):
    fig, ax = plt.subplots(ncols = 5, nrows = 2, figsize = (20, 6))
    ax = ax.flatten()
    for i, m in enumerate(model_list):
        dsn2.doy.sel(model = m).mean(['time']).plot(ax = ax[i], vmin = 100, vmax = 210)
    plt.suptitle('SSP-5.85, mean of 2080 - 2100 (far future)', fontsize = 16)
    plt.tight_layout()
    st.pyplot(fig)

else:
    st.write('This combination is not available')
