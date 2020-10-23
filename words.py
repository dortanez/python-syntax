def print_upper_words(words, must_start_with):
    '''
    prints each word in uppercase and starts with the entered letter
    '''

    for word in words:
        for letter in must_start_with:
            if word[0] == letter:
                print(word.upper())

    

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})

print_upper_words(["boy", "vroom", "car", "brush", "girl"], must_start_with={"c", "g", "b"})