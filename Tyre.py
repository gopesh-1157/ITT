# Take input: number of tyres
n = int(input('enter number of tyre: '))

# If tyres are divisible by 4
# (only 4-wheel vehicles → no 2-wheel combination possible)
if n % 4 == 0:
    print('NO')

# If remainder is 2
# (can form combination like 1 two-wheeler + some four-wheelers)
elif n % 4 == 2:
    print('YES')

# For all other cases (odd numbers, invalid combinations)
else:
    print('NO')
