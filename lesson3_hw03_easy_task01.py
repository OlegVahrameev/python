def my_round(number, ndigits):
    number = (number*(10**ndigits))//1
    return (number+1)/(10**ndigits)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

