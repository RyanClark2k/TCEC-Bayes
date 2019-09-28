from math import factorial as fact

total = 100
n = 14
w = 3
l = 1

wr = (w + 1) / (n + 2)
lr = (l + 1) / (n + 2)
dr = 1 - wr - lr
wp = 0

rem = total - n

for i in range(rem + 1):
    for j in range(rem - i + 1):
        k = rem - i - j
        coef = fact(rem) / (fact(i) * fact(j) * fact(k))
        p = coef * (wr**i) * (dr**j) * (lr**k)
        if i - k > l - w:
            wp += p

print('{}% chance of win'.format(round(wp, 3) * 100))