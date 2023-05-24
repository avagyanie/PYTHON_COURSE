"""
Գրել դեկորատոր, որը, բացի ֆունկցիան աշխատացնելուց, նաև վերադարձնում է՝ ինչքան ժամանակում է այն աշխատում։
"""

import time

def outer(func):
    def inner(sec):
        start = time.time()
        func(sec)
        end = time.time()
        result = end - start
        return f"Function new_func() works {result} soconds"
    return inner

@outer
def new_func(sec):
    time.sleep(sec)
    return 'Go to sleep'

x = new_func(5)

print(x)
