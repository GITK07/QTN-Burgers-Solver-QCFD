from qtn_solver import run_qtn_burgers
from classical_reference import run_classical_burgers
import matplotlib.pyplot as plt
import numpy as np
import csv
from pathlib import Path

Path("results/plots").mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    grid_size = 16
    time_steps = 20
    dt = 0.001
    nu = 0.01
    
    qtn = run_qtn_burgers(grid_size,time_steps,dt,nu)
    ref = run_classical_burgers(grid_size,time_steps,dt,nu)
    
    with open("results/validation.csv", "w", newline = "") as f:
        writer = csv.writer(f)
        writer.writerow(["Time", "L2 Error"])
        for t in range(time_steps+1):
            l2 = np.linalg.norm(ref[t]-qtn[t])
            writer.writerow([t,l2])
            
    for t in range(time_steps+1):
        plt.plot(ref[t], '--', label=f'Classcial t={t}')
        plt.plot(qtn[t], label=f'QTN t={t}')
            
plt.legend()
plt.title("QTN Solver vs Classical-Burgers")           
plt.savefig("results/plots/shock_profile.png")
plt.show()