# # codewars - even or odd
# def even_or_odd(number):
#   if int(number) % 2 == 0:
#     return "Even"
#   else:
#     return "Odd"


# # codewars - Numbers to strings
# def number_to_string(num):
#     return str(num)


def vowel_count(inputStr):
    inputStr.count("a", "e", "i", "o", "u")
    if inputStr == True:
        inputStr.count("a", "e", "i")
        inputStr.count("o", "u")
        print(inputStr.count("a", "e", "i") + inputStr.count("o", "u"))