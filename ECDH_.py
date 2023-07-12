from lab1 import *

def generate_shared_secret(curve, priv_key, pub_key):
    # Обчислює спільний секрет за протоколом ECDH

    # Обчислення спільної точки
    shared_point = scalar_mult(curve, priv_key, pub_key)

    # Використання X-координати спільної точки як спільного секрету
    shared_secret = shared_point.x

    return shared_secret

# Загальні системні параметри
curve = ECC.generate(curve='P-256')
base_point = base_point_get(curve)

# Генерація особистих ключів учасників
priv_key1 = getRandomInteger(256)
priv_key2 = getRandomInteger(256)

# Обчислення відкритих ключів
pub_key1 = scalar_mult(curve, priv_key1, base_point)
pub_key2 = scalar_mult(curve, priv_key2, base_point)

# Обмін відкритими ключами

# Обчислення спільного секрету для учасника 1
shared_secret1 = generate_shared_secret(curve, priv_key1, pub_key2)

# Обчислення спільного секрету для учасника 2
shared_secret2 = generate_shared_secret(curve, priv_key2, pub_key1)

# Перевірка, що спільні секрети співпадають
if shared_secret1 == shared_secret2:
    print("Спільні секрети співпадають!")
else:
    print("Спільні секрети не співпадають!")