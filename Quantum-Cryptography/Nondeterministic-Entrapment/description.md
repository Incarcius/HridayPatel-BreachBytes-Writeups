## Description

You wake up in a dimly lit quantum lab, surrounded by humming cryostats and flickering monitors.  
A message from **Professor Incarcius** flashes on the screen:

> “The flag is hidden within the quantum signals. Only those who see beyond the illusions can reveal what’s lost. The odds are in the rotations… but not every twist leads you to truth.”

You are given a sequence of measurement probabilities produced by a single‑qubit circuit that repeatedly applies rotations about the Y‑axis.  
For a single qubit, the probability of measuring |1⟩ after a rotation by angle \(theta\) around the Y‑axis is:

\[
P(1) = sin^2(theta/2)
\]

Some rotations are meaningful, others are decoys.  
Your task is to **reverse the observed probabilities**, recover hidden XOR relations between adjacent flag bytes, and use them to reconstruct the original flag.

The flag that generated these quantum readings:

- starts with `DJSISACA{`  
- ends with `}`  

### Hints

- Phase rotations (`rz`) only change the **global phase** of the state and do **not** affect measurement probabilities in the Z‑basis.
- The values you recover from probabilities in `recovered_candidates.py` are of the form \(a ^ b\), where \(a\) and \(b\) are adjacent flag characters. 

