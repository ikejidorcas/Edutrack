def factorial(val):
    val = float(input('Enter number'))
    if val ==1:
        return 1
    else:
        return val + factorial(val - 1)
print(factorial((300)))
