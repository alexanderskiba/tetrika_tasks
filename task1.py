def task(array):
    array = list(array)
    for index, value in enumerate(array):
        if int(value) == 0:
            return index

print(task("111111111111111111111111100000000"))


