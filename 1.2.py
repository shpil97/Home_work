my_list_cub = []
my_list_cub_2 = []
result_1 = 0

for i in range(1, 1001, 2):
    my_list_cub.append(i ** 3)

n_sum = 0
for n, val in enumerate(my_list_cub):
    n_sum = 0
    while val > 0:
        n_sum += val % 10
        val //= 10
    if n_sum % 7 == 0:
        result_1 += my_list_cub[n]
print(result_1)

for m in my_list_cub:
    my_list_cub_2.append(m + 17)
result_2 = 0
for n, val in enumerate(my_list_cub_2):
    n_sum = 0
    while val > 0:
        n_sum += val % 10
        val //= 10
    if n_sum % 7 == 0:
        result_2 += my_list_cub_2[n]
print(result_2)
