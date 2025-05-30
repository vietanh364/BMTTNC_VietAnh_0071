from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Route for home page
@app.route("/")
def home():
    return render_template('index.html')

# Route for Caesar Cipher page
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

# Route for encryption
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    try:
        text = request.form['inputPlainText']
        key = int(request.form['inputKeyPlain'])
        caesar_cipher = CaesarCipher()
        encrypted_text = caesar_cipher.encrypt(text, key)
        
        # Return both HTML and JSON responses
        if request.accept_mimetypes.accept_json:
            return jsonify({
                'status': 'success',
                'original_text': text,
                'key': key,
                'encrypted_text': encrypted_text
            })
        return render_template('caesar.html',
                            encrypted_result=encrypted_text,
                            plain_text=text,
                            encrypt_key=key)
    except Exception as e:
        if request.accept_mimetypes.accept_json:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 400
        return render_template('caesar.html',
                            error=f"Encryption error: {str(e)}")

# Route for decryption
@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    try:
        text = request.form['inputCipherText']
        key = int(request.form['inputKeyCipher'])
        caesar_cipher = CaesarCipher()
        decrypted_text = caesar_cipher.decrypt(text, key)
        
        # Return both HTML and JSON responses
        if request.accept_mimetypes.accept_json:
            return jsonify({
                'status': 'success',
                'original_text': text,
                'key': key,
                'decrypted_text': decrypted_text
            })
        return render_template('caesar.html',
                            decrypted_result=decrypted_text,
                            cipher_text=text,
                            decrypt_key=key)
    except Exception as e:
        if request.accept_mimetypes.accept_json:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 400
        return render_template('caesar.html',
                            error=f"Decryption error: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)