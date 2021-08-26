some_var = (2,)
if some_var is None:
    print("NoneType")
else:
    print(type(some_var))

a = None # пустая строка
b = a or 1
print(b, type(b))
