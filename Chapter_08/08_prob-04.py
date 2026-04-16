def Sum(num):
    if num == 0:
        return 0
    return num + Sum(num - 1)

sum = Sum(5)
print(sum)