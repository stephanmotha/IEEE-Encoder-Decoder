
def intToBin(num: int, bin: str):
    if len(bin)>32:
        return bin
    if num==0 and bin=='':
        return '0'

    elif num==0:
        return bin

    new = num // 2
    addedDigit = str(num%2)
    bin += addedDigit

    return intToBin(new, bin)


# print(intToBin(263, hi)[::-1])

def floatToBin(num: float, bin: str):
    if len(bin)>32:
        return bin
    if num==0 and bin=='':
        return '0'

    elif num==0:
        return bin

    temp = num*2
    addedDigit = str(temp)[0]
    new = float(str(num * 2)[1:])
    # print(new)
    bin += addedDigit

    return floatToBin(new, bin)

# print(floatToBin(0.1, ''))

def numToSciNot(num: float):
    wholeDecimal = ''


    if num<0:
        wholeDecimal = str(num)[1:].split(".")
    else:
        wholeDecimal = str(num).split(".")

    # if -1 < num < 1:


    # print(wholeDecimal)

    floatPortion = floatToBin(float("."+wholeDecimal[1]), '')

    # print(floatPortion)

    if -1 < num < 1:
        wholeBin = floatPortion
        exp = (wholeBin.find('1')+1)*-1

        print(wholeBin[abs(exp)-1:])
        print(exp)

        return [wholeBin[abs(exp)-1:], exp]

    # print(floatPortion)
    intPortion = intToBin(int(wholeDecimal[0]), '')[::-1]
    wholeBin = intPortion+floatPortion


    return [wholeBin, len(intPortion)-1]



def sciNotToIEEE(SciNot: list, original:float):
    # 1 sign bit
    signBit = ''
    if original>=0:
        signBit = '0'
    else:
        signBit = '1'

    # 8 exponent bits
    if SciNot[1] != 0:
        expBias = SciNot[1]+127
    else:
        expBias = 0

    expToBin = intToBin(expBias, '')[::-1]
    if len(expToBin)<8:
        expToBin = "0"*(8-len(expToBin)) + expToBin


    # 23 bit mantissa
    mantissa = SciNot[0][1:24]

    return signBit+expToBin+mantissa


def Decoder(num:float):
    sciNot = numToSciNot(float(num))

    answer = sciNotToIEEE(sciNot, num)
    if len(answer)<32:
        return answer+(32-len(answer))*"0"

    return answer

print(Decoder(0))


