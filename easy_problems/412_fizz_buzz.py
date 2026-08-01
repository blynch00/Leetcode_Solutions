def fizzBuzz(n: int) -> list[str]:
    return_arr = []
    for x in range(1, n + 1):
        if x % 3 == 0 and x % 5 != 0:
            return_arr.append("Fizz")
        elif x % 5 == 0 and x % 3 != 0:
            return_arr.append("Buzz")
        elif x % 15 == 0:
            return_arr.append("FizzBuzz")
        else:
            return_arr.append(x)
    return return_arr
print(fizzBuzz(5))