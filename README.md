![image.png](attachment:image.png)

The Burgers’ equation is a canonical nonlinear PDE that blends convective nonlinearity with viscous diffusion in a single scalar (1‑D) field. By stripping away the pressure term and incompressibility constraint of the full Navier–Stokes (NS) system, it retains the hardest 
parts of fluid motion, non‑linear steepening and viscous smoothing, while remaining analytically tractable. This makes Burgers an ideal entry‑level CFD benchmark and a low‑resource proving ground for quantum solvers. Because Burgers keeps the hard nonlinear/viscous core of 
NS, but omits pressure projection, any quantum‑classical splitting, Trotterisation, or tensor‑compression validated here will transfer directly to NS once a pressure solver is added. Resource counts obtained on Burgers therefore provide a lower‑bound estimate for full‑scale
Navier–Stokes workloads.

In the QTN (Quantum Tensor Network) approach, we represent the 1D velocity field of a fluid (a vector of numbers over space) in a compressed form using a Matrix Product State (MPS) — a structure from quantum physics used to efficiently describe high-dimensional vectors.
Instead of storing the full velocity field as a long vector, we break it into small matrices (tensors) that are multiplied together — this can save space and allow structured updates.
