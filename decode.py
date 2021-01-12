#using string
hi = ''

def intToBin(num: int, bin: str):
    if num==0 and bin=='':
        return 0

    elif num==0:
        return bin

    new = num // 2
    addedDigit = str(num%2)
    bin += addedDigit

    return intToBin(new, bin)


print(intToBin(263, hi)[::-1])


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


def floatToBin(num: float, bin: str):
    if len(bin)>15:
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

    return floatToBin(new, bin)

#(floatToBin(0.3, ''))

def numToSciNot(num: float):
    wholeDecimal = ''
    if num<0:
        wholeDecimal = str(num)[1:].split(".")
    else:
        wholeDecimal = str(num).split(".")


    intPortion = intToBin(int(wholeDecimal[0]), '')[::-1]
    floatPortion = floatToBin(float("."+wholeDecimal[1]), '')

    wholeBin = (intPortion+floatPortion)

    return [wholeBin, len(intPortion)-1]

#print(numToSciNot(263.3))

def sciNotToIEEE(SciNot: list, original:float):
    # 1 sign bit
    signBit = ''
    if original>0:
        signBit = '0'
    else:
        signBit = '1'

    # 8 exp bits
    expBias = SciNot[1]+127
    expToBin = intToBin(expBias, '')[::-1]
    print(expToBin)

    # 23 bit mantissa
    mantissa = SciNot[0][1:24]

    return signBit+expToBin+mantissa


def Decoder(num:float):
    sciNot = numToSciNot(num)
    return sciNotToIEEE(sciNot, num)

print(Decoder(263.3))
#11000011100000111010011001100110
#01000011100000111010011001100110