prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

# A

result = ''
for i in prices:
    result += f' {int(i // 1)} руб {int(100 * round((i % 1), 2) // 1):02} коп,'
print(result)

print('-' * 10)

# B

print(prices)
print(id(prices))
prices.sort()
print(prices)
print(id(prices))

print('-' * 10)

# C

prices_min = prices.copy()
prices_min.sort(reverse=True)
print(prices_min)
print(id(prices_min))

print('-' * 10)

# D

prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
# print(prices)
print(sorted(prices, reverse=True)[:5])
