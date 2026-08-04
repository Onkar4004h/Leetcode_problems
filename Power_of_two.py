def power_of_two(num):
    for x in range(1,int(num**0.5)+1):
     if 2**x == num:
        return True
    return False
print(power_of_two(3)) 