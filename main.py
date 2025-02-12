def word_count(string):
    words = string.split()
    count = len(words)
    return count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() # get the contents of the file
        words = word_count(file_contents) # get the word count
        print(words)
        return words

main()