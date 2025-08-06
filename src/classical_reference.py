import numpy as np

def run_classical_burgers(grid_size, time_steps, dt, nu):
    u = np.ones(grid_size)
    u[grid_size//2:] = 0
    results = [u.copy()]
    
    for _ in range(time_steps):
        u_new = u.copy()
        for i in range(1, grid_size-1):
            dx = 1.0/grid_size
            adv = u[i]*(u[i+1]-u[i-1])/(2*dx)
            visc = nu*(u[i+1]-2*u[i]+u[i-1])/dx**2
            u_new[i] = u[i]-dt*adv +dt*visc
        u = u_new
        results.append(u.copy())
    return results