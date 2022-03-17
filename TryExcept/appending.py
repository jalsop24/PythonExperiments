

some_list = []


try:
    for i in range(10):
        some_list.append(i)

    raise RuntimeError
except Exception:
    pass

print(some_list)
