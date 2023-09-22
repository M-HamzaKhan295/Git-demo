def multiply(numbers):
    result = 1
    for x in numbers:
        result *= x
    return result


numbers_list = [1, 2, 3,4]
multiply_result = multiply(numbers_list)
print("Multiply: ", multiply_result)

