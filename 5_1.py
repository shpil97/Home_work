def odd_nums_gen(nums):
    for n in range(1, nums + 1, 2):
        yield n


odd_to_nums = odd_nums_gen(int(input()))
print(next(odd_to_nums))
print(next(odd_to_nums))
print(list((odd_to_nums)))
