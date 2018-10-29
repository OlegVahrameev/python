import random
lst_gen = [random.randint(0, 10) for _ in range(10)]
print('lst_gen = ', lst_gen)
lst_x2 = [el*2 for el in lst_gen]
print('lst_x2 = ', lst_x2)

# # или
# lst_x2 = list(map(lambda x: x * 2, lst_gen))
# print('lst_x2 = ', lst_x2)