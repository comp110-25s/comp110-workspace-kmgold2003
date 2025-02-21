def fizzbuzz(n : int) -> str:
    '''practice quiz function'''
    if n % 3 == 0 and n % 5 != 0:
        return "fizz"
    if n % 3 != 0 and n % 5 == 0:
        return "buzz"
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    else:
        return str(n)
    

print(fizzbuzz(15))