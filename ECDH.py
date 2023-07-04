from cryptography.hazmat.primitives.asymmetric import ec

def generate_shared_secret(curve, priv_key, pub_key):
    private_key = ec.derive_private_key(priv_key, curve)
    shared_key = private_key.exchange(ec.ECDH(), pub_key)

    # Використання X-координати спільного ключа як результуючого спільного секрету
    shared_secret = shared_key[:32]

    return shared_secret

def main():
    # Загальні параметри
    curve = ec.SECP256R1()  # Використовуйте потрібну криву

    # Особистий ключ та відкритий ключ учасника 1(Antona)
    priv_key_anton = ec.generate_private_key(curve)
    pub_key_anton = priv_key_anton.public_key()

    # Особистий ключ та відкритий ключ учасника 2(Maksa)
    priv_key_maks = ec.generate_private_key(curve)
    pub_key_maks = priv_key_maks.public_key()

    # Генерація спільного секрету
    shared_secret1 = generate_shared_secret(curve, priv_key_anton.private_numbers().private_value, pub_key_maks)
    shared_secret2 = generate_shared_secret(curve, priv_key_maks.private_numbers().private_value, pub_key_anton)

    # Перевірка, що спільні секрети співпадають
    if shared_secret1 == shared_secret2:
        print("Спільні секрети співпадають:", shared_secret1.hex())
    else:
        print("Спільні секрети не співпадають.")

if __name__ == "__main__":
    main()
