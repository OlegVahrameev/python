import random
lst_gen = [random.randint(-10, 10) for _ in range(10)]
print('lst_gen = ', lst_gen)
lst_new = [i for i in lst_gen if i % 3 == 0 and i > 0 and i % 4 != 0]
print('lst_new = ', lst_new)