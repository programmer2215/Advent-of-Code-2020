

# SETUP
fh = open("input.txt", "r")
nums = []
for num in fh:
    nums.append(int(num))

# PART-1
for i in nums:
    for j in nums:
        sum = i + j
        if sum == 2020:
            num_1 = i
            num_2 = j
            product = num_1 * num_2
            break
    

print(f"{num_1} + {num_2} = {num_1 + num_2}")
print(f'{num_1} * {num_2} = {product}')

# PART-2
for i in nums:
    for j in nums:
        for k in nums:
            sum = i + j + k
            if sum == 2020:
                num_1 = i
                num_2 = j
                num_3 = k
                product = num_1 * num_2 * num_3
                break
        
    
print(f"{num_1} + {num_2} + {num_3} = {num_1 + num_2 + num_3}")
print(f'{num_1} * {num_2} * {num_3} = {product}')