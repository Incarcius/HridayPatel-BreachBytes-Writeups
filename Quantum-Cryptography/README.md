# Quantum Cryptography Challenges

This folder contains the quantum cryptography challenge I authored for BreachBytes 3.0, focused on exploiting the math behind single‑qubit rotations and measurement statistics.

## Challenge list

- **Nondeterministic Entrapment** (hard)  
  A noisy-looking quantum random number generator where each flag byte pair is hidden in the probability of measuring \(|1⟩\) after a Y‑axis rotation. Players must:
  - Use \(P(1) = \sin^2(\theta/2)\) to invert measurement probabilities back to rotation angles.  
  - Recover candidate \(a ^ b\) values for adjacent flag characters and refine them using a helper script.  
  - Exploit XOR properties and the known flag structure `DJSISACA{...}` to walk the XOR chain and reconstruct the full flag from the recovered relations.

