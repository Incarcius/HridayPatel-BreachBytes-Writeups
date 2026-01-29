import random
from Crypto.Util.number import bytes_to_long, getPrime

a12z98 = b'12345678910111213'
           
t = 7   # no. of shares required to recover the key  
n = 15  # no. of shares to generate 

p1 = 144617414729854976017
p2 = 144617414729854976027

c34x76 = bytes_to_long(a12z98)

b23y87 = getPrime(c34x76.bit_length() + 1) 
print(f"Chosen b23y87 : {b23y87}")

if c34x76 > b23y87:
    raise ValueError("b23y87 too small!")

e56v54 = [random.randint(0, b23y87-1) for _ in range(t-1)]
e56v54.insert(2, c34x76)  

d45w65 = []
for i in range(1, n+1):
    f67u43 = p1 if (i % 2) else p2
    g78t32 = 0
    for j, c in enumerate(e56v54):
        g78t32 = (g78t32 + c * pow(i, j, b23y87)) % b23y87
    g78t32 = g78t32 % f67u43
    d45w65.append((i, g78t32, f67u43))

print(f"Secret length (bytes): {len(a12z98)}\n")
print("Shares from Shamirs Shared Secrets (x, y, mod):\n")
for s in d45w65:
    print(f"{s}\n")

