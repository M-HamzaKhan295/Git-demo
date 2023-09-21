def Tables(number):
    for count in range(1,11):
        Product= count * number 
        print(number ,'x' ,count ,'=',Product)
    print("")
    for count in range(1,11): 
        Sum = count + number
        print(number ,'+' ,count ,'=',Sum )



number = int(input('Enter a number '))
Tables(number)
