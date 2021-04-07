# 25P
# Write a function that takes in a string as argument and returns a tuple after performing the following actions:
# - the string is split after the first encountered space.
# - all letters in the first half will be transformed to upper case letters
# - all characters that are not lower-case letters in the second half will be replaced with "_"
# - returned tuple contains the two processed strings
# example: "1234567a Text to te5t" will become ("1234567A", "_ext_to_te_t")

data = "1234567a Text to te5t"


def process_text(text):
    str1 = ''      # we declare 2 empty strings
    str2 = ''

    for i in text:
        if i == ' ':
            str1 = text[:text.index(i) + 1] # the first empty string becomes the first half
            str2 = text[text.index(i) + 1:] # the second empty string becomes the second half
            str1 = str1.upper()  # we change all the letters from the first half into upper case letters
    for j in str2:
        if ord(j) <= 90:        # using the position in the ASCII table we check to see if a letter from the second half is lower,upper or is an empty space
            str2 = str2.replace(j,'_') # we replace the upper case letters and the empty spaces with '_'


    return str1,str2   # we return the two halves

print(process_text(data))








