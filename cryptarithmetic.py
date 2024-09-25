from itertools import permutations

def crypt_arithmetic():
    for perm in permutations('0123456789', 8):
        s, e, n, d, m, o, r, y = perm
        if m == '0':
            continue
        send = int(s + e + n + d)
        more = int(m + o + r + e)
        money = int(m + o + n + e + y)
        if send + more == money:
            return send, more, money

# Example usage
send, more, money = crypt_arithmetic()
print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
