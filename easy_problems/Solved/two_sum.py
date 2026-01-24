nums = [2,7,11,15] 
target = 9
return_list = []
for index, x in enumerate(nums):
    print(x)
    print(index)
    second_number = target - x
    for second_index, y in enumerate(nums):
        if y == second_number:
            return_list.append(index)
            return_list.append(second_index)
            break

print(return_list)