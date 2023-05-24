"Գրել դեկորատոր, որը ստուգում է, թե ինչ տիպի փոփոխական է վերադարձվում։"


def outer(func):
    def inner(*args):
        res = func(*args)
        x = set()    #Յուրաքանչյուր տիպը 1 անգամ տպելու համար, եթե պետք է ամեն անգամ տպել, կարելի է լիստ սահմանել
        for i in args:
            x.add(type(i))
        return x
    return inner

@outer
def new_func(*args):
    
    return "Hello"

a = new_func(2, "anun", 3.12, [1, 2, 3], (1, 1, 1), {4, 5, 6}, {"a": 1, "b": 2}, 120)

print(a)
