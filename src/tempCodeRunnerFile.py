from qtn_solver import run_qtn_burgers
from classical_reference import run_classical_burgers
import matplotlib.pyplot as plt
import numpy as np
import csv
import os

os.makedirs("results/plots", exist_ok=True)

if __name__ == "__main__":
    grid_size = 16
    time_steps = 3
    dt = 0.001
    nu = 0.01
    
    qtn = run_qtn_burgers(grid_size