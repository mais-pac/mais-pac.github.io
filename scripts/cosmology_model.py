"""Numerical checks and explicitly synthetic teaching data.
Benchmark: H0=70 km/s/Mpc, Om=0.3, OL=0.7, no radiation at late times.
"""
from math import sqrt, log, asinh, pi
from pathlib import Path
import csv, json

C = 299792.458                 # km/s
KM_PER_MPC = 3.0856775814913673e19
SEC_PER_GYR = 3.15576e16
G = 6.6743e-11
SIGMA = 5.670374419e-8
WIEN = 2.897771955e-3
T0 = 2.725
H0, OM, OL = 70.0, 0.3, 0.7


def simpson(f, a, b, n=4096):
    n += n % 2
    h = (b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+i*h) for i in range(1,n,2))+2*sum(f(a+i*h) for i in range(2,n,2)))


def E(z, om=OM, ol=OL, orad=0.0):
    ok = 1-om-ol-orad
    return sqrt(orad*(1+z)**4+om*(1+z)**3+ok*(1+z)**2+ol)


def hubble_time_gyr(h0=H0):
    return KM_PER_MPC/h0/SEC_PER_GYR


def comoving_gpc(z, h0=H0, om=OM, ol=OL, orad=0.0):
    return (C/h0/1000)*simpson(lambda x: 1/E(x,om,ol,orad),0,z)


def lookback_gyr(z, h0=H0, om=OM, ol=OL, orad=0.0):
    return hubble_time_gyr(h0)*simpson(lambda x: 1/((1+x)*E(x,om,ol,orad)),0,z)


def age_gyr(h0=H0, om=OM, ol=OL, orad=0.0):
    if orad == 0 and abs(om+ol-1)<1e-12 and om>0 and ol>0:
        return hubble_time_gyr(h0)*2/(3*sqrt(ol))*asinh(sqrt(ol/om))
    # Accurate enough for the late-time models used in this handout.
    return hubble_time_gyr(h0)*simpson(lambda x: 1/((1+x)*E(x,om,ol,orad)),0,1e8,16384)


def horizons(h0=H0, om=OM, ol=OL):
    dh = C/h0/1000
    particle = dh*2*simpson(lambda y: 1/sqrt(om+ol*y**6),0,1)
    event = dh*simpson(lambda u: 1/sqrt(ol+om*u**3),0,1) if ol>0 else float('inf')
    return particle,event


def synthetic_data():
    """Low-z linear-law teaching data. NOT a real survey catalogue."""
    zs = [0.010,0.015,0.020,0.028,0.035,0.045,0.055,0.065,0.080,0.095,0.115,0.140]
    noise = [210,-180,130,-100,160,-140,80,120,-110,70,-60,100]
    return [{'id':f'S{i:02d}','z':z,'distance_mpc':round(C*z/72,2),
             'velocity_km_s':round(C*z+n,2),'sigma_velocity_km_s':200.0}
            for i,(z,n) in enumerate(zip(zs,noise),1)]


def fit(rows):
    sxx=sum(r['distance_mpc']**2 for r in rows)
    h=sum(r['distance_mpc']*r['velocity_km_s'] for r in rows)/sxx
    err=sqrt(sum((r['distance_mpc']*r['sigma_velocity_km_s'])**2 for r in rows))/sxx
    rms=sqrt(sum((r['velocity_km_s']-h*r['distance_mpc'])**2 for r in rows)/len(rows))
    return h,err,rms


def values():
    hc=H0/KM_PER_MPC
    rhoc=3*hc*hc/(8*pi*G)
    ug=4*SIGMA/(C*1000)*T0**4
    vals={
        'hubble_time_gyr':hubble_time_gyr(),
        'hubble_distance_gpc':C/H0/1000,
        'critical_density':rhoc,
        'critical_energy_density':rhoc*(C*1000)**2,
        'cmb_energy_density':ug,
        'omega_gamma':ug/(rhoc*(C*1000)**2),
        'z_m_lambda':(OL/OM)**(1/3)-1,
        'z_acc':(2*OL/OM)**(1/3)-1,
        'age_benchmark':age_gyr(),
        'age_eds':2/3*hubble_time_gyr(),
        'particle_horizon_gpc':horizons()[0],
        'event_horizon_gpc':horizons()[1],
    }
    for z in [1,2,3,5.82]:
        dc=comoving_gpc(z)
        vals[f'z{z}']={'DC_Gpc':dc,'DL_Gpc':dc*(1+z),'DA_Gpc':dc/(1+z),
                       'lookback_Gyr':lookback_gyr(z),'emission_age_Gyr':age_gyr()-lookback_gyr(z),
                       'recession_c':dc/(C/H0/1000)}
    vals['mit_quasar']={'DC_Gly':comoving_gpc(5.82,65,.35,.65)*3.261563777,
                        'age_Gyr':age_gyr(65,.35,.65),
                        'emission_age_Gyr':age_gyr(65,.35,.65)-lookback_gyr(5.82,65,.35,.65)}
    vals['baao']={'observed_nm':486.1*1.3,'linear_distance_mpc':C*.3/72,
                  'linear_lookback_gyr':.3*hubble_time_gyr(72),
                  'exact_lookback_gyr':lookback_gyr(.3,72),
                  'exact_DL_mpc':1000*comoving_gpc(.3,72)*1.3}
    vals['rocket']={'threshold_km_s':10*H0,'time_gyr_1500':-log(1-700/1500)*hubble_time_gyr()}
    h100=100/KM_PER_MPC
    rho100=3*h100*h100/(8*pi*G)
    og100=(4*SIGMA/(C*1000)*10**4)/(rho100*(C*1000)**2)
    vals['yale_omega_gamma_h2']=og100
    vals['yale_equal_coefficient']=1/(2.5*og100)
    rows=synthetic_data()
    vals['hubble_all']=fit(rows)
    vals['hubble_cut']=fit([r for r in rows if r['z']>=.03])
    vals['dark_energy_problem']={'u_lambda':(rhoc-2.8e-27)*(C*1000)**2,
                                'z_equal':((rhoc-2.8e-27)/2.8e-27)**(1/3)-1,
                                'z_acc':(2*(rhoc-2.8e-27)/2.8e-27)**(1/3)-1}
    vals['cmb_problem']={'T':WIEN/.0005,'z':WIEN/.0005/T0-1,
                         'eds_age_gyr':2/3*hubble_time_gyr()*(WIEN/.0005/T0)**(-1.5),
                         'benchmark_age_gyr':age_gyr()-lookback_gyr(WIEN/.0005/T0-1)}
    return vals,rows

if __name__=='__main__':
    vals,rows=values()
    out=Path(__file__).resolve().parents[1]/'handouts'/'data'
    out.mkdir(parents=True,exist_ok=True)
    (out/'cosmology-values.json').write_text(json.dumps(vals,indent=2))
    with (out/'hubble-practice.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    print(json.dumps(vals,indent=2))
