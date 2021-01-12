# Convert IEEE-754 to Decimal 

# Read the sign bit, exponential bits, and mantissa
def encoder(binary_string):

    sign_bit = binary_string[0]
    exponent_val = calc_exp_val(binary_string[1:9])
    exp_bias = exponent_val - 127
    mantissa_val = calc_mantissa_val(binary_string[9:])

    return general_form(sign_bit, mantissa_val, exp_bias, binary_string[1:9], binary_string[9:], exponent_val) 


# Calculate exponential value
def calc_exp_val(exp_bits):

    val = 0
    curr_exp = 7
    for i in exp_bits:
        val += int(i) * (2  curr_exp)
        curr_exp -= 1
    return val


# Calculate mantissa value
def calc_mantissa_val(mantissa_bits):

    val = 0
    curr_exp = -1
    for i in mantissa_bits:
        val += int(i) * (2  curr_exp)
        curr_exp -= 1
    return val


# Calculate general form of decimal value and return all relevant information 
# about the values 
def general_form(sign_bit, mantissa_val, exp_bias, exponent_bits, mantissa, exp_val):

    sign = (-1) ** int(sign_bit)
    val = 1 + mantissa_val
    exp = 2 ** exp_bias


    return [sign_bit, exponent_bits, exp_val, exp_bias, mantissa,  mantissa_val, sign * val * exp]
