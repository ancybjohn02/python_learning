def replace_char(input_string, char_To_replace, replacement_char):
    return ''.join(map(lambda x : replacement_char if x == char_To_replace else x, input_string))


input_string = input(" Enter the string : ")
char_To_replace =  input("char to be replaced : ")
replacement_char = input("to be replaced with :")
output = replace_char(input_string, char_To_replace, replacement_char)
print(output)