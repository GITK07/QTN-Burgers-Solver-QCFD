import numpy as np
import tntorch as tn

def run_qtn_burgers(grid_size, time_steps, dt, nu):
    u = np.ones(grid_size)
    u[grid_size//2:] = 0
    
    u_tt = tn.Tensor(u.reshape([2]*int(np.log2(grid_size))))
    results = [u_tt.full().flatten()]
    
    dx = 1.0/grid_size
    
    for t in range(time_steps):
        u_full = u_tt.full().flatten()
        adv = u_full*np.gradient(u_full, dx)
        
        visc = nu*np.gradient(np.gradient(u_full, dx),dx)
        u_next = u_full-dt*adv+dt*visc
        
        u_tt = tn.Tensor(u_next.reshape([2]*int(np.log2(grid_size))), ranks_tt=8)
        results.append(u_tt.full().flatten())
    return results
        
