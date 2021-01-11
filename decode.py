hi = ''

def wholeToBin(num: int, bin: str):
    if num==0 and bin=='':
        bin += 0

    if num==0:

        return None

    new = num // 2
    addedDigit = str(num%2)
    bin += addedDigit
    print(bin)
    wholeToBin(new, bin)
    return bin


wholeToBin(263, hi)
print(hi)


sample = []


def wholeToBin(num: int, bin: list):
    if num==0 and bin==[]:
        bin += 0

    if num==0:

        return None

    new = num // 2
    addedDigit = str(num%2)
    bin.append(addedDigit)
    #print(bin)
    wholeToBin(new, bin)


wholeToBin(263, hi)
print(''.join(hi.sample()))


