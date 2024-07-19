def xor_encrypt_decrypt(text, key):
    """Enkripsi atau dekripsi teks menggunakan XOR dengan kunci."""
    encrypted_decrypted_text = ''
    key_length = len(key)
    i = 0
    for char in text:
        encrypted_decrypted_text += chr(ord(char) ^ ord(key[i]))
        i = (i + 1) % key_length
    return encrypted_decrypted_text


def main():
    print("Hallo, Selamat datang di program enkripsi dan dekripsi XOR.")

    # Input plainteks dan kunci
    plain_text = input("Masukkan plainteks: ").strip()
    if not plain_text:
        print("Error: Plainteks tidak boleh kosong!")
        return
    
    key = input("Masukkan Kata kunci (untuk enkripsi): ").strip()
    if not key:
        print("Error: Kunci tidak boleh kosong!")
        return

    # Enkripsi
    cipher_text = xor_encrypt_decrypt(plain_text, key)
    print(f"Hasil Enkripsi: {cipher_text}")

    # Input kunci untuk dekripsi
    key_decrypt = input("Masukkan Kata kunci (untuk dekripsi): ").strip()
    if key_decrypt != key:
        print("Error: Kunci untuk dekripsi tidak sesuai!")
        return
    
    # Dekripsi
    decrypted_text = xor_encrypt_decrypt(cipher_text, key_decrypt)
    print(f"Hasil Dekripsi: {decrypted_text}")


if __name__ == "__main__":
    main()
