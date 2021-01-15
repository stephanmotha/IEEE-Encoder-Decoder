import pygame

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TAN = (210, 180, 140)
BABY_BLUE = (137, 207, 240)
pygame.init()

# Set the width and height of the screen [width, height]
WIDTH = 1660
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()


def int_to_bin(num: int, bin: str):
    if len(bin) > 32:
        return bin
    if num == 0 and bin == '':
        return '0'

    elif num == 0:
        return bin

    new = num // 2
    added_digit = str(num % 2)
    bin += added_digit

    return int_to_bin(new, bin)


def float_to_bin(num: float, bin: str):
    if len(bin) > 32:
        return bin
    if num == 0 and bin == '':
        return "0"

    elif num == 0:
        return bin

    temp = num * 2
    added_digit = str(temp)[0]
    new = float(str(num * 2)[1:])

    bin += added_digit

    return float_to_bin(new, bin)


def num_to_sci_not(num: float):

    if num < 0:
        whole_decimal = str(num)[1:].split(".")
    else:
        whole_decimal = str(num).split(".")

    float_portion = float_to_bin(float("." + whole_decimal[1]), '')

    if -1 < num < 1:
        whole_bin = float_portion
        exp = (whole_bin.find('1') + 1) * -1

        return [whole_bin[abs(exp) - 1:], exp]

    int_portion = int_to_bin(int(whole_decimal[0]), '')[::-1]

    if float_portion != '0':
        whole_bin = int_portion + float_portion

    else:
        whole_bin = int_portion

    return [whole_bin, len(int_portion) - 1]


def sci_not_to_ieee(sci_not: list, original: float):

    if original >= 0:
        sign_bit = '0'
    else:
        sign_bit = '1'

    if sci_not[1] != 0 or sci_not[0] == '1':
        exp_bias = sci_not[1] + 127
    else:
        exp_bias = 0

    exp_to_bin = int_to_bin(exp_bias, '')[::-1]
    if len(exp_to_bin) < 8:
        exp_to_bin = "0" * (8 - len(exp_to_bin)) + exp_to_bin

    mantissa_ = sci_not[0][1:24]

    return sign_bit + exp_to_bin + mantissa_


def decoder_calc_main(num):
    sci_not = num_to_sci_not(float(num))

    answer = sci_not_to_ieee(sci_not, num)
    if len(answer) < 32:
        answer = answer + (32 - len(answer)) * "0"

    font = pygame.font.SysFont('Calibri', 60, True, False)
    new = answer[0] + " - " + answer[1:9] + " - " + answer[9:]
    ans_display = font.render("Answer:  " + new, True, BLACK)
    screen.blit(ans_display, [175, 600])
    font3 = pygame.font.SysFont('Calibri', 20, True, False)
    pygame.draw.rect(screen, BABY_BLUE, [25, 700, 115, 70])
    back = font3.render("Back to Start", True, BLACK)
    screen.blit(back, [28, 725])
    sign = font3.render("Sign (1 Bit)", True, WHITE)
    ex = font3.render("Exponent: (8 bits)", True, WHITE)
    manti = font3.render("Mantissa: (23 bits)", True, WHITE)
    screen.blit(sign, [380, 575])
    screen.blit(ex, [520, 575])
    screen.blit(manti, [1050, 575])


def encoder_calc_main(s):
    font = pygame.font.SysFont('Calibri', 35, True, False)
    font2 = pygame.font.SysFont('Calibri', 60, True, False)
    font3 = pygame.font.SysFont('Calibri', 20, True, False)
    sf = font.render("Sign: (1 bit)", True, WHITE)
    screen.blit(sf, [120, 360])
    pygame.draw.rect(screen, BLACK, [140, 400, 75, 80], 3)
    ex = font.render("Exponent: (8 bits)", True, WHITE)
    screen.blit(ex, [380, 360])
    pygame.draw.rect(screen, BLACK, [375, 400, 275, 80], 3)
    manti = font.render("Mantissa: (23 bits)", True, WHITE)
    screen.blit(manti, [1050, 360])
    pygame.draw.rect(screen, BLACK, [800, 400, 750, 80], 3)
    print(s)
    if s == "000000000000000000000000000000000":
        ans = font2.render("ANSWER: " + str("0.0"), True, BLACK)
        screen.blit(ans, [600, 700])
        sfval = font2.render("0", True, BLACK)
        screen.blit(sfval, [160, 415])
        exval = font2.render("00000000", True, BLACK)
        screen.blit(exval, [395, 415])
        man_val = font2.render("00000000000000000000000", True, BLACK)
        screen.blit(man_val, [815, 415])

    elif len(s) > 0:

        sign = s[0]
        s = s[1:]

        expo = exponent(s[:8])
        man = mantissa(s[8:])
        sfval = font2.render(str(sign), True, BLACK)
        screen.blit(sfval, [160, 415])
        exval = font2.render(str(s[:8]), True, BLACK)
        screen.blit(exval, [395, 415])
        man_val = font2.render(str(s[8:]), True, BLACK)
        screen.blit(man_val, [815, 415])
        ans = (-1) ** (int(sign)) * (1 + man) * (2 ** expo)
        ans_text = font2.render(
            " = (-1)^ " + str(sign) + " x ( 1 + " + str(man) + " ) x 2^ " + str(
                expo), True, BLACK)
        screen.blit(ans_text, [300, 600])
        ans_display = font2.render("ANSWER: " + str(ans), True, BLACK)
        screen.blit(ans_display, [600, 700])
    pygame.draw.rect(screen, BABY_BLUE, [25, 700, 115, 70])
    back = font3.render("Back to Start", True, BLACK)
    screen.blit(back, [28, 725])


def exponent(s):
    val = 0
    i = 0
    counter = 7
    while i < len(s):
        val += int(s[i]) * (2 ** counter)
        counter -= 1
        i += 1

    return val - 127


def mantissa(s):
    val = 0
    i = 0
    counter = -1
    while i < len(s):
        val += int(s[i]) * (2 ** counter)
        i += 1
        counter -= 1
    return val


def decode_display():
    screen.fill(TAN)
    font = pygame.font.SysFont('Calibri', 60, True, False)
    go = font.render("Go", True, WHITE)
    pygame.draw.rect(screen, BLACK, [450, 100, 700, 45], 4)
    pygame.draw.rect(screen, GREEN, [1200, 100, 125, 85])
    screen.blit(go, [1230, 115])

    pygame.display.flip()


def encode_display():
    screen.fill(TAN)
    font = pygame.font.SysFont('Calibri', 60, True, False)
    go = font.render("Go", True, WHITE)
    pygame.draw.rect(screen, BLACK, [450, 100, 700, 45], 4)
    pygame.draw.rect(screen, GREEN, [1200, 100, 125, 85])
    screen.blit(go, [1230, 115])

    pygame.display.flip()


def start():
    screen.fill(TAN)

    font = pygame.font.SysFont('Calibri', 100, True, False)
    font2 = pygame.font.SysFont('Calibri', 50, True, False)
    font3 = pygame.font.SysFont('Calibri', 20, True, False)
    names = font3.render(
        "By: Sahib Nanda, Stephan Motha and Dale Rodrigues",
        True, BLACK)
    screen.blit(names, [1200, 770])
    text = font.render("IEEE 754 Encoder/ Decoder (32 Bit)", True, BABY_BLUE)
    screen.blit(text, [80, 100])
    pygame.draw.rect(screen, WHITE, [550, 400, 200, 100])
    pygame.draw.rect(screen, WHITE, [950, 400, 200, 100])
    en_text = font2.render("Encode", True, BABY_BLUE)
    de_text = font2.render("Decode", True, BABY_BLUE)
    screen.blit(de_text, [570, 430])
    screen.blit(en_text, [970, 430])


text = ""
pointer = "start"
font_type = pygame.font.SysFont('Calibri', 42, True, False)
# -------- Main Program Loop -----------


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()
            if 550 <= position[0] <= 750 and 400 <= position[1] <= 500:
                # decode
                decode_display()
                pointer = "decode"
            elif 950 <= position[0] <= 1150 and 400 <= position[1] <= 500:
                # encode
                encode_display()
                pointer = "encode"
            elif 1200 <= position[0] <= 1325 and 100 <= position[1] <= 185:

                if pointer == "encode":

                    pointer = "encode_calculation"
                    encoder_calc_main(text)

                elif pointer == "decode":
                    pointer = "decode_calc"

                    if len(text) > 0:

                        decoder_calc_main(float(text))
                    else:
                        font3 = pygame.font.SysFont('Calibri', 20, True, False)
                        pygame.draw.rect(screen, BABY_BLUE, [25, 700, 115, 70])
                        back = font3.render("Back to Start", True, BLACK)
                        screen.blit(back, [28, 725])
            elif 25 <= position[0] <= 140 and 700 <= position[1] <= 770:

                pointer = "start"
                text = ""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:

                text = text[:-1]

            else:
                if len(text) < 33 and (pointer == "encode"
                                       or pointer == "decode"):

                    text += event.unicode
        if pointer == "encode":
            encode_display()
            display_text = font_type.render(text, True, BLACK)
            screen.blit(display_text, [450, 100])
        elif pointer == "decode":
            decode_display()
            display_text = font_type.render(text, True, BLACK)
            screen.blit(display_text, [450, 100])
        elif pointer == "start":
            start()

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    # --- Drawing code should go here
    if pointer == "start":
        start()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(20)

# Close the window and quit.
pygame.quit()
