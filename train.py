def powersum(power, *args):
    #Return the sum of each argument raised to the specified power.
    total = 0
    for i in args:
        total += pow(i, power)
    return total

#function call
print(powersum(2, 3, 4))