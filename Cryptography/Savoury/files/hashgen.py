import hashlib
import random
from salt_file import base_salt, passwords

possible_passwords = [
"travy", "babybaby", "whyyyyy", "Utube", "aliceinwonderland", "maxtergalindo", "aryamdon", "decjanfeb", "Nebunika",
"calbaby", "lizzywithlucyha", "jakedogg", "panc4ke06", "acj1354236", "mollybuzz", "briansgrl123", "b1n2c3",
"trippersz", "miera5807", "REYPEREZ", "shnuggles", "ahuvah", "jezewski", "tummytree347", "ccla2255", "22649981916",
"TEODIOANDREA", "3610458", "072117542", "travis2448", "yamazen", "Loyalty6", "gukbfr", "69010", "mohawk513",
"artacsp10785", "maude22", "fluffy46", "cavyice26", "dorisdej", "REVO33", "facatativa", "masuilene", "yaye06",
"hineman", "alidol27", "newtitou", "letmein", "servant4God", "3127872950", "thezombie", "deia123", "amg305",
"ya07di02ra94", "gazelle102", "hirobaby", "112930632", "rojapel10", "carlobecerra1995", "pollly102", "ahmedhayat",
"jesuschick2010", "geolcoa", "byntsnq", "ventures", "carla123456", "504jay", "breane", "emilyyy", "greg51",
"smokita", "maeres88", "3dogsrule", "2006-1993", "adinadan", "44always", "7SILVIARAU", "password123", "saliha",
"ladyt5", "daresk", "emzie18180", "cailing", "mmahmoodh123", "mallocalloc", "wipes08", "33plates",
"mitapa", "bryanteamo", "bodyart4u", "7506495i", "jorge011503", "m32008", "0819627238", "gazeebo", "whooo123",
"mrcvrazed45", "paulinarocks", "m01p09p05", "CARMENIG"
]


digits = [str(i) for i in range(10)] # 0 to 9
suffixes = [chr(i) for i in range(ord('a'), ord('z') + 1)] \
    + [chr(i) for i in range(ord('A'), ord('Z') + 1)] \
    + ['!', '@', '#', '%', '&']


chosen_digits = [random.choice(digits) for _ in passwords]
chosen_suffixes = [random.choice(suffixes) for _ in passwords]


hashes = []
for i in range(len(passwords)):
    pw = passwords[i]
    digit = chosen_digits[i]
    suffix = chosen_suffixes[i]
    salt = base_salt + digit + suffix

    if i % 2 == 0:
        password_hash = hashlib.sha256(hashlib.md5((pw + salt).encode()).digest()).hexdigest()
    else:
        password_hash = hashlib.sha256(hashlib.md5((salt + pw).encode()).digest()).hexdigest()

    hashes.append(password_hash)

print("\nHash Table:\n")
for i, h in enumerate(hashes):
    print(f"{i}: {h}")
