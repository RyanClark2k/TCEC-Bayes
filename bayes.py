from math import factorial as fact

total = 100   # Total games in series.
n = 14        # Total games so far.
w = 3         # Total wins so far.
l = 1         # Total losses so far.
draws = True  # Are there draws in this tournament?


correction = 3 if draws else 2
wr = (w + 1) / (n + correction)
lr = (l + 1) / (n + correction)
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