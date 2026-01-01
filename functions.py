def co_prime(a, b):
    while b:
        a, b = b, a % b
    if (a==1):
      return True
    else:
      return False

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None  # Inverse doesn't exist
    else:
        return x % m