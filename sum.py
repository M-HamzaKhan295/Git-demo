def Sum(numbers):
    total = 0                                           
                                                
    for x in numbers:
        total += x
    return total
numbers = [1, 2, 3, 4]
print("Sum is :",Sum(numbers))
