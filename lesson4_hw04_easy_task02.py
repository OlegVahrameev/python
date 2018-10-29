fruits1 = ["груша", "банан", "яблоко", "ананас"]
fruits2 = ["манго", "ананас", "апельсин", "груша"]
fruits = list(set(fruits1) & set(fruits2))
print('fruits = ', fruits)