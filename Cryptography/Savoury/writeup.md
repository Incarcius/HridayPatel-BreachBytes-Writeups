### Step 1: Understanding the hashing scheme

The challenge uses 15 randomly chosen passwords from a provided wordlist of 100 candidates.  
For each chosen password, the script:

- Picks a random digit `d` from `0–9`.  
- Picks a random suffix character `s` (a–z, A–Z, or one of `! @ # % &`).  
- Combines a base salt, the digit, and the suffix into a salt string.  
- Depending on whether the current index is odd or even, it either:
  - concatenates `password + salt`, or  
  - concatenates `salt + password`.  

The final hash is computed as:

1. Compute `md5` of the concatenated string.  
2. Compute `sha256` of the resulting `md5` digest.  

Our goal is to recover, for each of the 15 hashes:

- The password used.  
- The digit and suffix appended to the base salt.  
- The base salt itself (hinted in the description by the word “pepper”).

From the flavor text, it is natural to assume the base salt is `"pepper"`, which turns out to be correct.

### Step 2: Brute forcing the combinations

Since the wordlist, the digit range, and the suffix alphabet are all reasonably small, we can brute force each hash by trying:

- every password in the provided list,  
- every digit from `0` to `9`,  
- every allowed suffix character,  
- and both concatenation orders (salt before password or after password).

A simple brute force script in Python could look like this:

```python
import hashlib

possible_passwords = [
    "travy", "babybaby", "whyyyyy", "Utube", "aliceinwonderland",
    "maxtergalindo", "aryamdon", "decjanfeb", "Nebunika",
    "calbaby", "lizzywithlucyha", "jakedogg", "panc4ke06",
    "acj1354236", "mollybuzz", "briansgrl123", "b1n2c3",
    "trippersz", "miera5807", "REYPEREZ", "shnuggles", "ahuvah",
    "jezewski", "tummytree347", "ccla2255", "22649981916",
    "TEODIOANDREA", "3610458", "072117542", "travis2448", "yamazen",
    "Loyalty6", "gukbfr", "69010", "mohawk513",
    "artacsp10785", "maude22", "fluffy46", "cavyice26", "dorisdej",
    "REVO33", "facatativa", "masuilene", "yaye06",
    "hineman", "alidol27", "newtitou", "letmein", "servant4God",
    "3127872950", "thezombie", "deia123", "amg305",
    "ya07di02ra94", "gazelle102", "hirobaby", "112930632",
    "rojapel10", "carlobecerra1995", "pollly102", "ahmedhayat",
    "jesuschick2010", "geolcoa", "byntsnq", "ventures", "carla123456",
    "504jay", "breane", "emilyyy", "greg51",
    "smokita", "maeres88", "3dogsrule", "2006-1993", "adinadan",
    "44always", "7SILVIARAU", "password123", "saliha",
    "ladyt5", "daresk", "emzie18180", "cailing", "mmahmoodh123",
    "mallocalloc", "wipes08", "33plates",
    "mitapa", "bryanteamo", "bodyart4u", "7506495i", "jorge011503",
    "m32008", "0819627238", "gazeebo", "whooo123",
    "mrcvrazed45", "paulinarocks", "m01p09p05", "CARMENIG"
]

digits = [str(i) for i in range(10)]
suffixes = (
    [chr(i) for i in range(ord('a'), ord('z') + 1)] +
    [chr(i) for i in range(ord('A'), ord('Z') + 1)] +
    ['!', '@', '#', '%', '&']
)

base_salt = "pepper"

hash_input = input("Enter hash: ").strip()
opt = input("Enter 1 for even index (password+salt) or 0 for odd index (salt+password): ").strip()

found = None

for pw in possible_passwords:
    for d in digits:
        for s in suffixes:
            salt = base_salt + d + s

            if opt == '1':
                candidate = pw + salt
            elif opt == '0':
                candidate = salt + pw
            else:
                continue

            sha256_hash = hashlib.sha256(
                hashlib.md5(candidate.encode()).digest()
            ).hexdigest()

            if sha256_hash == hash_input:
                found = candidate
                break
        if found:
            break
    if found:
        break

if found:
    print("Match found:", found)
else:
    print("No match found for hash:", hash_input)
```

You can either crack the hashes one by one by passing each hash interactively, or extend the script to loop over all 15 hashes in a list and record the results automatically.

### Step 3: Recovered passwords and salts

Running the brute force across all 15 hashes yields the following matches (index corresponds to the hash position):

- **Index 0**: password `shnuggles`, salt `pepper7R`  
  - Effective string: `shnugglespepper7R`
- **Index 1**: password `CARMENIG`, salt `pepper8y`  
  - Effective string: `pepper8yCARMENIG`
- **Index 2**: password `ya07di02ra94`, salt `pepper2t`  
  - Effective string: `ya07di02ra94pepper2t`
- **Index 3**: password `maxtergalindo`, salt `pepper8T`  
  - Effective string: `pepper8Tmaxtergalindo`
- **Index 4**: password `password123`, salt `pepper0e`  
  - Effective string: `password123pepper0e`
- **Index 5**: password `hirobaby`, salt `pepper0L`  
  - Effective string: `pepper0Lhirobaby`
- **Index 6**: password `letmein`, salt `pepper2#`  
  - Effective string: `letmeinpepper2#`
- **Index 7**: password `daresk`, salt `pepper2X`  
  - Effective string: `pepper2Xdaresk`
- **Index 8**: password `mollybuzz`, salt `pepper4X`  
  - Effective string: `mollybuzzpepper4X`
- **Index 9**: password `panc4ke06`, salt `pepper4R`  
  - Effective string: `pepper4Rpanc4ke06`
- **Index 10**: password `briansgrl123`, salt `pepper7w`  
  - Effective string: `briansgrl123pepper7w`
- **Index 11**: password `thezombie`, salt `pepper1p`  
  - Effective string: `pepper1pthezombie`
- **Index 12**: password `gazelle102`, salt `pepper4p`  
  - Effective string: `gazelle102pepper4p`
- **Index 13**: password `carlobecerra1995`, salt `pepper8@`  
  - Effective string: `pepper8@carlobecerra1995`
- **Index 14**: password `emilyyy`, salt `pepper3Z`  
  - Effective string: `emilyyypepper3Z`

From each of these, we can extract the corresponding triplet:

- First letter of the password  
- The digit used in the salt  
- The suffix character used in the salt  

For example:

- Index 0 (`shnuggles`, `pepper7R`) → `s7R`  
- Index 1 (`CARMENIG`, `pepper8y`) → `C8y`  
- Index 2 (`ya07di02ra94`, `pepper2t`) → `y2t`  
- … and so on.

### Step 4: Constructing the flag

Using the format given in the problem statement:

```text
DJSISACA{<triplet1>_<triplet2>_..._<triplet15>_<base_salt>}
```
and the extracted triplets from the recovered data, we obtain:

```text
DJSISACA{s7R_C8y_y2t_m8T_p0e_h0L_l2#_d2X_m4X_p4R_b7w_t1p_g4p_c8@_e3Z_pepper}
```
