def closest_power(base, num):
    if num == 1:
        return 0
    else:
        i = 0
        while i < num:
            if base ** i >= num:
                return i
            else:
                if num - base**i < num - base**(i+1):
                    return i
                else:
                    if num - base**i <= abs(num - base**(i+1)):
                        return i
                    else:
                        i += 1
input1 = float(input('base? '))
input2 = float(input('num? '))
print(closest_power(input1, input2))
