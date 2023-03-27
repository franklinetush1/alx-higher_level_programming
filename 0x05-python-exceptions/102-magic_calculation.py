#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for z in range(1, 3):
        try:
            if z > a:
                raise Exception('Too far')
            else:
                result += a ** b / z
        except:
            result = b + a
            break
    return (result)
