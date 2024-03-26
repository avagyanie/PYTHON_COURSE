"Գրել դեկորատոր, որը ստուգում է, թե ինչ տիպի փոփոխական է վերադարձվում։"


def dec(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        result = set()   #Յուրաքանչյուր տիպը 1 անգամ տպելու համար, եթե պետք է ամեն անգամ տպել, կարելի է լիստ սահմանել
        for i in args:
            result.add(type(i))
        for j in kwargs.values():
            result.add(type(j))

        return result
    return wrapper

@dec
def f(*args, **kwargs):
    
    print("There are all types of positional and keyword arguments!")

print(f(1, 'Ani', [1, 2, 3], a = 12, b = {1: 'x', 2: 'y'}))
