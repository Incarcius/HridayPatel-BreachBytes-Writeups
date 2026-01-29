### Step 1: Understanding the setup

We are given an obfuscated `chal.py` and an `output.txt` file.  
The `output.txt` contains the length of the secret in bytes and 15 Shamir shares.  

From the challenge name and the code (specifically the line:

```python
print("Shares from Shamirs Shared Secrets (x, y, mod):\n")
```
we can confirm that the scheme used is Shamir's Secret Sharing.
In this scheme, a secret is split into multiple shares, and the original secret can only be reconstructed if at least a threshold number of shares is available.

From `chal_obs.py`, we see that the threshold for this challenge is 7 shares.
The 15 shares we are given are generated over two different moduli, `p1` and `p2`, which alternate during share generation.

### Step 2: Grouping shares by modulus

Since the shares alternate between two primes, we first separate them according to their modulus:

```python
from sympy import mod_inverse

# ---- SHARES ----
shares = [
    (1, 119851754009690660916, 144617414729854976017),
    (2, 37991115101738800321, 144617414729854976027),
    (3, 69163871120902756702, 144617414729854976017),
    (4, 69544837930006065004, 144617414729854976027),
    (5, 76659971158768438387, 144617414729854976017),
    (6, 43868527434343164463, 144617414729854976027),
    (7, 115595609094483204434, 144617414729854976017),
    (8, 3210196247551954359, 144617414729854976027),
    (9, 143590095238310798554, 144617414729854976017),
    (10, 137009597012602961873, 144617414729854976027),
    (11, 127577839959426928703, 144617414729854976017),
    (12, 14575911154724053845, 144617414729854976027),
    (13, 102924801761451620259, 144617414729854976017),
    (14, 88523782506687773742, 144617414729854976027),
    (15, 43163861931617331069, 144617414729854976017)
]

# ---- SEGREGATE BY MODULUS ----
p1 = 144617414729854976017
p2 = 144617414729854976027

shares_p1 = [(x, y) for x, y, mod in shares if mod == p1]
shares_p2 = [(x, y) for x, y, mod in shares if mod == p2]
```
Now `shares_p1` contains all shares over `p1`, and `shares_p2` contains all shares over `p2`.

### Step 3: Recovering the partial secrets with Lagrange interpolation

To reconstruct the secret under each modulus, we apply Lagrange interpolation at \(x = 0\).  
Using any 7 shares (the threshold) for each modulus is sufficient.

```python
# ---- LAGRANGE INTERPOLATION AT x = 0 ----
def lagrange_interpolate_zero(points, mod):
    total = 0
    for i, (x_i, y_i) in enumerate(points):
        num, den = 1, 1
        for j, (x_j, _) in enumerate(points):
            if i != j:
                num = (num * (-x_j)) % mod
                den = (den * (x_i - x_j)) % mod
        total = (total + y_i * num * mod_inverse(den, mod)) % mod
    return total

s_p1 = lagrange_interpolate_zero(shares_p1[:7], p1)
s_p2 = lagrange_interpolate_zero(shares_p2[:7], p2)

print(f"Secret mod p1: {s_p1}")
print(f"Secret mod p2: {s_p2}")
```
This yields:

```text
Secret mod p1: 120691705935694332047
Secret mod p2: 55266033081063690396
```
So we now know:
- secret ≡ 120691705935694332047 (mod p1)
- secret ≡ 55266033081063690396 (mod p2)


