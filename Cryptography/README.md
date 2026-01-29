# Cryptography Challenges

This folder contains the cryptography challenges I authored for BreachBytes 3.0.

## Challenge list

- **Emoji Madness** (easy)  
  Pangram‑based emoji substitution where players infer a monoalphabetic key from emoji mappings, then decrypt the full message.

- **Savoury** (easy)  
  Salted hash cracking: players receive a hashing script, multiple hashes, and a wordlist, and must brute‑force the unknown salt and plaintexts.

- **Our Essay** (medium)  
  RSA with OSINT‑style hints: players are given the encryption code, public exponent, and ciphertext, and must derive \(p\) and \(q\) from contextual hints before performing standard RSA decryption.

- **Shameless Shamir** (medium)  
  Shamir’s Secret Sharing with two primes: from 15 shares and a threshold of 7, players reconstruct partial secrets over two different fields and combine them using the Chinese Remainder Theorem.

- **Secp32k1** (hard)  
  ECC over a composite modulus where the field splits into a 2016‑bit and a 32‑bit prime; players solve the discrete log on the small curve, then use partial key information to brute‑force the full private key.

- **The Lost Cipher of Isla de Muerta** (hard)  
  Two‑stage web oracle: first recover the key of an Affine‑style layer around AES‑CBC using chosen‑plaintext queries, then use it to craft inputs that flip the identity string and reveal the final FLAG_KEY.
