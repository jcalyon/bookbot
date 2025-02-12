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

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() # get the contents of the file
        words = word_count(file_contents) # get the word count
        chars = char_freq(file_contents) # calc the char frequency
        print(chars)
        return words

main()