# BreachBytes 3.0 – Challenge Set

This repository contains the challenges I authored for **BreachBytes 3.0**, an on‑site Jeopardy‑style Capture The Flag competition organized by the ISACA student chapter at Dwarkadas J. Sanghvi College of Engineering (DJSCE), Mumbai, in October 2025.

## Event overview ##

- Format: On‑site Jeopardy‑style CTF (single‑day, 12 hours)
- Organizer: DJSCE ISACA Student Chapter
- Role: Challenge Author (Cryptography, Quantum, Misc/Stego)
- Challenges authored:
  - 6 × Cryptography (classical + hybrids)
  - 1 × Quantum cryptography
  - 2 × Miscellaneous

A more detailed event description and responsibilities are in [`overview/event.md`](overview/event.md).

## Repository Structure ##

- `Cryptography/` – Classical and modern cryptography challenges (some with reversing or web components)
- `Quantum-Cryptography/` – Quantum / quantum‑inspired cryptography
- `Miscellaneous/` – Cryptography and stego‑focused  hybrid challenges

Each challenge folder will contain:

- `description.md` – Player‑facing challenge description and files
- `writeup.md` – Intended solution and reasoning
- `files/` – Handouts given to participants
- `src/` – Source code for generators, servers, or internal logic

Flags in this repository are redacted or slightly altered so that the challenges are not directly reusable in future events.

