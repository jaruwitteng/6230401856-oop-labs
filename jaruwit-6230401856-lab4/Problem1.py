product = 1 # change product to 0
for i in range(1, 10):   #change range to 1, 10
    product *= i
print("product is {}".format(product))

sum_squares = 0
for i in range(10):
    i_sq = i**2
    sum_squares += i_sq   #make this line inside for range
print("sum_squares is {}".format(sum_squares))

nums = 0
for num in range(10):
    nums += num     #num need to be nums
print("nums is {}".format(nums))