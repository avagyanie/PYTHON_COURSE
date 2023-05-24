"""
Գրել դեկորատոր, որը, բացի ֆունկցիան աշխատացնելուց, նաև վերադարձնում է՝ ինչքան ժամանակում է այն աշխատում։
"""

import time

def outer(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        result = end - start
        return result
    return inner

@outer
def new_func():
    res = time.sleep(5)
    return res

x = new_func()

print(x)
