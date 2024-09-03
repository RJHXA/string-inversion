def reverse_string(s):
    char_list = list(s)
    length = len(char_list)
    
    i = 0
    j = length - 1
    
    while i < j:
        char_list[i], char_list[j] = char_list[j], char_list[i]
        i += 1
        j -= 1
    
    return ''.join(char_list)


input_string = input("Enter the string to be reversed: ")

reversed_string = reverse_string(input_string)
print(f"Reversed string: {reversed_string}")
