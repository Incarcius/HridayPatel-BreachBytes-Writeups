from secret_logic import next_prime_after, what_cipher_is_this, who_is_the_prime_suspect
import random



def MR(n):
    n = int(n)
    if n <= 2:
        return 2
    if n % 2 == 0:
        n += 1
    while not who_is_the_prime_suspect(n):
        n += 2	#bWF4a3ggaGd2eCBwdGwgdCB6eGdibmwgZ3RmeHcgeXhrZnRtIHBhaCBpa2hpaGx4dyBlYm1tZXggbWF4aGt4Zmw7IG1ha3h4IHZ4Z21ua2J4bCBldG14ayB2dGtmYnZhdHhlIHdibHZob3hreHcgbWF4YmsgZWJmYm10bWJoZ2wgdGd3IG5nd3hrIHQgdnhnbW5rciB0eW14ayBtYXRtLCBtYWhseCBlYmZibXRtYmhnbCBweGt4IHliZ3RlZXIgaG94a3ZoZnggdXIgdCBJa2JmeCBsbmxpeHZtLg==
	return n



a = 738
e = 65537
p = next_prime_after(a)



def gen_q(p):
    width = 512
    bin_p = bin(p)[2:].zfill(width)
    rev_p = int(bin_p[::-1], 2)

    seed = what_cipher_is_this(p, last_digits=15)
    #Hint:r854947296677o6749738844398777m564856494539744563e

    rnd = random.Random(seed)
    mask = rnd.getrandbits(width)

    candidate = rev_p ^ mask

    if candidate % 2 == 0:
        candidate += 1
    q = MR(candidate)

    return q



q = gen_q(p)

N = p*q

with open("flag.txt", "r", encoding="utf-8") as f:
    pt_str = f.read().strip()
pt_bytes = pt_str.encode("utf=8")
pt = int.from_bytes(pt_bytes, "big")

ct = pow( pt, e, N)

print(f"ct : {ct}")
print(f"E : {e}")