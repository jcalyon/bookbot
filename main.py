def word_count(string):
    words = string.split()
    count = len(words)
    return count

def char_freq(string):
    char_dict = {}
    for char in string:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def report(file, words, chars):
    
    # print the top line
    print(f"--- Begin report of {file} ---")

    # print the word count
    print(f"{words} words found in the document \n")

    # print the alphabetic char frequency
    for char in chars:
        #conditional check if alphabet
        if char.isalpha():
            print(f"The '{char}' character was found {chars[char]} times")
        else:
            next

    # print the end line
    print(f"--- End report ---")
    return

def main():
    file = "books/frankenstein.txt"
    with open(file) as f:
        file_contents = f.read() # get the contents of the file
        
        words = word_count(file_contents) # get the word count
        chars = char_freq(file_contents) # calc the char frequency
        report(file, words, chars) #run a print report on the word count and character frequency
        
        # print(chars)
        return words

main()