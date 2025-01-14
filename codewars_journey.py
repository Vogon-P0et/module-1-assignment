# codewars | even or odd
# Description:
# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
def even_or_odd(number):
  if int(number) % 2 == 0:
    return "Even"
  else:
    return "Odd"

test_num = 34
print(even_or_odd(test_num))


# codewars | Numbers to strings
# the simplest answer to the "numbers to strings" problem seems to be type casting to a string
def number_to_string(num):
    return str(num)

test_str_to_num = "78908765456789"
print(type(number_to_string(test_str_to_num)))


# codewars | vowel count
# this was actually harder than expected. I tried a few times to get an answer without using a list.
# I think a list comprehension would also have worked but I actually understand loops better than list comprehensions at this moment
def vowel_count(Str):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in Str:
        if char in vowels:
            count += 1
    return(count)

test_vowel_count = "i want to count the number of values in a string"
print(vowel_count(test_vowel_count))