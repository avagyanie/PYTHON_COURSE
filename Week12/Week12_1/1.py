"""
Գրել դեկորատոր, որը, բացի ֆունկցիան աշխատացնելուց, նաև վերադարձնում է՝ ինչքան ժամանակում է այն աշխատում։
"""

import time

def outer(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        result = end - start
        print(f"Function new_func() works {result} soconds")
        return result
    return inner

@outer
def new_func(*args, **kwargs):
    time.sleep(1)
    print("Go to sleep")

x = new_func()

print(x)
