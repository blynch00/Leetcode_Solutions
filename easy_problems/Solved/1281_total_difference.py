def subtractProductAndSum(n: int) -> int:
    string_n = str(n)
    product = 1
    total_sum = 0
    for x in range(0, len(string_n)):
        product = product * int(string_n[x])
    print(product)
    for y in range(0, len(string_n)):
        total_sum = total_sum + int(string_n[y])
    print(total_sum)
    total_difference = product - total_sum
    return total_difference


print(subtractProductAndSum(234))
