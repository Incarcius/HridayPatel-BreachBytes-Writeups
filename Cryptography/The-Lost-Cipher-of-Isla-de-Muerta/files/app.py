import jwt
import os
import datetime
from flask import Flask, render_template, request, jsonify, make_response, redirect, url_for
from dotenv import load_dotenv

load_dotenv()

A = 11
B = 17
BLOCK_SIZE = 16
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHA_IDX = {c: i for i, c in enumerate(ALPHABET)}
A_inv = pow(A, -1, len(ALPHABET))
pad_char = 'H'

key_1 = os.getenv("KEY_1")
key_2 = os.getenv("KEY_2")
IV = os.getenv("IV")
FLAG_key = os.getenv("FLAG_KEY")
Flag = os.getenv("FLAG")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")


# -- level 1 --
def to_num(text):
    clean = ''.join(c for c in text.upper() if c in ALPHABET)
    clean = (clean + pad_char * BLOCK_SIZE)[:BLOCK_SIZE]
    return [ALPHA_IDX[c] for c in clean]

def encrypt_logic(plaintext, key_str, iv_str):
    key = to_num(key_str)
    iv = to_num(iv_str)
    pt = to_num(plaintext)
    ct = []
    for i in range(BLOCK_SIZE):
        p = pt[i]
        k = key[i]
        c_prev = iv[i] if i == 0 else ct[i - 1]
        c = (A * p + B * c_prev + k) % len(ALPHABET)
        ct.append(c)
    return ''.join(ALPHABET[x] for x in ct)

def decrypt_logic(ciphertext, key_str, iv_str):
    key = to_num(key_str)
    iv = to_num(iv_str)
    ct = to_num(ciphertext)
    pt = []
    for i in range(BLOCK_SIZE):
        c = ct[i]
        k = key[i]
        c_prev = iv[i] if i == 0 else ct[i - 1]
        p = (A_inv * (c - B * c_prev - k)) % len(ALPHABET)
        pt.append(p)
    return ''.join(ALPHABET[x] for x in pt)

# -- level 2 --
def clean_text(text):
    return ''.join(c for c in text if c.isalpha()).upper()

def to_indices(text):
    return [ALPHA_IDX[c] for c in text]

def test_identity(u_indices, key_indices, m_indices):
    pt_indices = []
    for i in range(len(m_indices)):
        c = u_indices[i]
        k = key_indices[i]
        c_prev = m_indices[i] if i == 0 else u_indices[i-1]
        p = (A_inv * (c - B * c_prev - k)) % len(ALPHABET)
        pt_indices.append(p)
    return ''.join(ALPHABET[x] for x in pt_indices)

def bracket_line(s):
    return ' '.join(f'({c})' for c in s)

def underline_line(s):
    return ' '.join(f' {c} ' for c in s)


@app.route('/')
def level1():
    token = request.cookies.get('token')
    if not token:
        token = jwt.encode({
            'level2': False,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        resp = make_response(render_template("level1.html"))
        resp.set_cookie('token', token)
        return resp
    return render_template("level1.html")

@app.route('/lv1_enc', methods=['POST'])
def encrypt():
    plaintext = request.form['plaintext']
    ciphertext = encrypt_logic(plaintext, key_1, IV)
    return jsonify({'ciphertext': ciphertext})

@app.route('/lv1_dec', methods=['POST'])
def decrypt():
    ciphertext = request.form['ciphertext']
    plaintext = decrypt_logic(ciphertext, key_1, IV)
    return jsonify({'plaintext': plaintext})

@app.route('/lv1_keycheck', methods=['POST'])
def check_key():
    submitted_key = request.form.get('key')
    if submitted_key and submitted_key.upper() == key_1.upper():
        token = jwt.encode({
            'level2': True,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        resp = make_response(jsonify({'message': 'That be the key! The way forward is clear.'}))
        resp.set_cookie('token', token)
        return resp
    else:
        return jsonify({'error': "Nay, that key unlocks naught. Try again, matey."}), 400

@app.route('/lv2')
def level2():
    token = request.cookies.get('token')
    if not token:
        return render_template("lock.html")
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        if data.get('level2'):
            return render_template("level2.html")
        else:
            return render_template("lock.html")
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return render_template("lock.html")

@app.route('/lv2_pad', methods=['POST'])
def pad():
    unpadded_input = request.form.get('unpadded_input', '')
    clean = ''.join(c for c in unpadded_input if c.isalpha()).upper()
    padded = (clean + pad_char * BLOCK_SIZE)[:BLOCK_SIZE]
    return f"Ahoy matey! Yer padded text: {padded}"

@app.route('/lv2_test', methods=['POST'])
def test():
    user_input = request.form.get('user_input', '')
    cleaned = clean_text(user_input)
    Original_ciphertext = "QWHUCKNFISFHICSPGRKOGJSGYQDCNFZP"
    if len(cleaned) != 2 * BLOCK_SIZE:
        return "Error: Input must be 32 letters (A-Z). Use the padding helper if ye need.", 400

    M_str = cleaned[:BLOCK_SIZE]
    U_str = cleaned[BLOCK_SIZE:]

    KEY_indices = to_indices(key_2)
    M_indices = to_indices(M_str)
    U_indices = to_indices(U_str)

    Padded_decrypted_identity = test_identity(U_indices, KEY_indices, M_indices)
    decrypted_identity = Padded_decrypted_identity[:11]

    brackets_row = bracket_line(cleaned)
    underline_row = underline_line(Original_ciphertext)

    output = (
        f"Original Identity: STRANDEDPIRATE\n\n"
        f"Your Input:\t{brackets_row}\n"
        f"Original :\t{underline_row}\n\n"
        f"Current Identity: {decrypted_identity}"
    )
    if decrypted_identity == "CAPTAINJACK":
        output += f"\n\nSuccess! Here be the Pirate’s reward: {FLAG_key}"
    
    resp = make_response(output)
    resp.headers['Content-Type'] = 'text/plain'
    return resp

@app.route('/lv2_keycheck', methods=['POST'])
def check_key_flag():
    key = request.form.get('key', '')
    if key.upper() == FLAG_key.upper():
        return Flag
    else:
        return "Ye key be cursed! Try again or walk the plank!"


if __name__ == '__main__':
    app.run(debug=False)

