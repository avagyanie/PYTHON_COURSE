
# def randfloat(start: float, end: float)->float:
#     import random
#     for i in range(start, end + 1):
#         a = random.random() * i
#     return a
# print(randfloat(1, 17))



# def randfloat(start: float, end: float)->float:
#     import random
#     a = random.sample(range(start, end), 2)
#     a[1] = str(a[1])
#     a[0] = str(a[0])
#     print(".".join(a))

# randfloat(0, 17)



def randfloat(start: float, end: float)->float:
    import random
    return random.uniform(start, end)

print(randfloat(1, 17))
