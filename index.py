def squared_set(num):
    return{x**2 for x in num}

set = {1, 2, 3, 6}
result = squared_set(set)
print(result)