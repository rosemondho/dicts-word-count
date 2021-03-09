# Read file 
# Tokenize the file by space
# Make the dictionary from

def find_words_count(filename):
    words=[]
    file=open(filename)

    for line in file:
        words.extend(line.rstrip().split(' '))

    return words


def create_dictionary(words):
    word_count={}

    for word in words:
        # put the words in the dictionary
        word = word.lower().strip('?!,.:()')
        word_count[word] = word_count.get(word, 0) + 1

    word_count = dict(sorted(word_count.items(), key=lambda kv: kv[1]))

    for word, count in word_count.items():
        print(word, count)
    return word_count


        


words=find_words_count('test.txt')
create_dictionary(words)