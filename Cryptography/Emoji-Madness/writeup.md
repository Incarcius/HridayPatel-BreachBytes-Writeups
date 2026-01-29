# Emoji Madness – Writeup

## Idea

The challenge description hints at **pangrams** (“short sentences which include all the alphabets”).  
The ciphertext is a sequence of emojis; once we identify the pangram used for the first sentence, we can treat the puzzle as a monoalphabetic substitution from letters to emojis and recover the full plaintext.

## Step 1 – Using the pangram hint

The hint suggests searching for sentences that contain every letter of the alphabet.  
A quick search for pangrams returns several candidates for eg.
1. [https://www.rd.com/list/fun-pangrams/](https://www.rd.com/list/fun-pangrams/)
2. [https://www.orchidsinternationalschool.com/blog/pangrams](https://www.orchidsinternationalschool.com/blog/pangrams)
3. [https://en.wikipedia.org/wiki/Pangram](https://en.wikipedia.org/wiki/Pangram)
Comparing their lengths and structure with the first emoji sentence, one common pangram matches well:

> `The five boxing wizards jump quickly`

We assume this is the plaintext of the first emoji sentence.

## Step 2 – Building the emoji–letter key

By aligning each position of the pangram with the corresponding emoji, we derive the substitution key.  
- A = 😂  
- B = 😊  
- C = 🤣  
- D = 👌  
- E = 😁  
- F = 😢  
- G = 🙌  
- H = 😎  
- I = 🤞  
- J = 😍  
- K = ❤️  
- L = 🙂  
- M = 😉  
- N = 🤗  
- O = 🤩  
- P = 😮  
- Q = 😆  
- R = 😘  
- S = 👍  
- T = 😑  
- U = 😒  
- V = 😶  
- W = 🫡  
- X = 😣  
- Y = 🤑  
- Z = 😴  

## Step 3 – Decrypting the full message

Once we have the mapping, we apply it to the entire emoji ciphertext.  
Decrypting all emoji characters with the key yields:

> `THE FIVE BOXING WIZARDS JUMP QUICKLY. THE FLAG IS THE LAST WORD. THE FLAG IS PANGRAMSENTENCES.`

From the text, the last word is clearly indicated as the flag value:

- Raw flag word: `PANGRAMSENTENCES`

Wrapping this in the standard CTF format gives:

```text
DJSISACA{PANGRAMSENTENCES}
