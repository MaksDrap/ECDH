from Crypto.Util.number import getRandomInteger
from Crypto.PublicKey import ECC

def base_point_get(curve):
    # Отримати базову точку G
    return curve.pointQ

def ec_point_gen(curve, x, y):
    # Створити точку ЕК з координатами (x, y)
    return curve.point(x, y)

def is_on_curve_check(curve, point):
    # Перевірити, чи належить точка point до кривої
    return curve.contains(point)

def add_ec_points(curve, a, b):
    # Додати точки a і b на ЕК
    return a + b

def double_ec_point(curve, a):
    # Подвоїти точку a на ЕК
    return 2 * a

def scalar_mult(curve, k, a):
    # Помножити точку a на скаляр k
    return k * a

def ec_point_to_string(point):
    # Перетворити точку в рядок
    return f"{point.x},{point.y}"

def string_to_ec_point(curve, s):
    # Перетворити рядок в точку
    x, y = map(int, s.split(","))
    return curve.point(x, y)

def print_ec_point(point):
    # Вивести координати точки на ЕК
    print(f"({point.x}, {point.y})")


curve = ECC.generate(curve='P-256')
G = base_point_get(curve)
k = getRandomInteger(256)
d = getRandomInteger(256)

H1 = scalar_mult(curve, d, G)
H2 = scalar_mult(curve, k, H1)

H3 = scalar_mult(curve, k, G)
H4 = scalar_mult(curve, d, H3)

result = H2 == H4

