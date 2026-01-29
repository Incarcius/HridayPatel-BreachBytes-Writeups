# BreachBytes 3.0 – Event Overview

## Context

- Name: BreachBytes 3.0 – Capture The Flag
- Type: On‑site Jeopardy‑style CTF
- Organizer: ISACA Student Chapter, Dwarkadas J. Sanghvi College of Engineering (DJSCE), Mumbai
- Timeline:
  - Challenge design and testing: September–October 2025
  - Competition day: 30th October 2025 (single‑day event, 12 hours)

## Role and responsibilities

- Served in the Tech & Cybersecurity department as a **challenge author** focusing on:
  - Cryptography (6 challenges: emoji-based cryptanalysis, hashing, RSA, Shamir’s Secret Sharing, ECC, hybrid web crypto)
  - Quantum cryptography (1 challenge using Qiskit and QRNG concepts)
  - Misc / Stego (2 challenges combining visual clues, classical ciphers and custom encodings)
- Designed end‑to‑end challenges:
  - Ideation, cryptographic design, implementation, and internal writeups
  - Generation of handout files, images and scripts
  - Basic deployment/testing for web‑backed challenges (e.g., Flask AES‑CBC oracle)

## Design goals

- Provide an accessible on‑ramp for beginners through easy crypto/stego problems such as emoji‑based substitution and visual binary art.
- Intentionally create **uncommon, hybrid challenges** so that players encountered techniques they would not usually see in standard CTFs, encouraging them to learn new tools and lines of thought.
- Include medium and hard tasks that require combining multiple skills:
  - OSINT‑style interpretation of hints for RSA parameters.
  - Number theory and discrete logarithms on elliptic curves with a composite base field.
  - Secret sharing reconstruction over two primes plus CRT.
  - Quantum measurement statistics followed by classical XOR‑based recovery of the flag.

## Note:-

This repository serves as the archived version of the challenges I personally authored.
Infrastructure, scoring, and additional categories (if any) were handled by the broader BreachBytes 3.0 organizing team.
    

