def square_numbers(nums):
    for num in nums:
        yield num ** 2


l = [1, 2, 3, 4]
ans = square_numbers(l)
for i in ans:
    print(i)

square = [x ** 2 for x in [1, 2, 3, 4]]
print(square)


square = (x ** 2 for x in [1, 2, 3, 4])
print(next(square))
print(next(square))
print(next(square))
print(next(square))
