import hashlib

def blake2(message):
    # You need to define digest_size or pass it as an argument.
    # For example, using the default 64 bytes for BLAKE2b:
    blake2_hash = hashlib.blake2b(digest_size=64) 
    blake2_hash.update(message)
    return blake2_hash.digest()

def main():
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    hashed_text = blake2(text)

    print('Chuỗi văn bản đã nhập:', text.decode('utf-8'))
    print('BLAKE2 Hash:', hashed_text.hex())

if __name__ == "__main__":
    main()