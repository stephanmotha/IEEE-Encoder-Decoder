#using string
hi = ''

def wholeToBin(num: int, bin: str):
    if num==0 and bin=='':
        return 0

    elif num==0:
        return bin

    new = num // 2
    addedDigit = str(num%2)
    bin += addedDigit

    return wholeToBin(new, bin)


print(wholeToBin(263, hi)[::-1])


#using list
# sample = []
# def wholeToBin(num: int, bin: list):
#     if num==0 and bin==[]:
#         bin.append(0)
#
#     if num==0:
#         return None
#
#     new = num // 2
#     addedDigit = str(num%2)
#     bin.append(addedDigit)
#
#     wholeToBin(new, bin)
#
# sample.reverse()
# wholeToBin(263, sample)
# print(''.join(sample))


def decimalToBin(num: int, bin: str):
    if len(bin)>10:
        return bin
    if num==0 and bin=='':
        return 0

    elif num==0:
        return bin


    temp = num*2
    addedDigit = str(temp)[0]
    new = float(str(num * 2)[1:])
    print(new)
    bin += addedDigit

    return decimalToBin(new, bin)

print(decimalToBin(0.3, ''))