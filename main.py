from wordcloud import WordCloud
import sys

#remove punctuations from a text
def remove_pun(text, punctuations):
    l = []
    for c in text:
        if c.isalpha() or c.isspace():
            l.append(c)
    text = ''.join(l)
    return text

#remove unintresting words from a line
def rm_un_words_l(line, uninteresting_words):
    linewords = line.split()
    resultwords = [word for word in linewords if word not in uninteresting_words]
    result = ' '.join(resultwords)
    return result

#remove unintresting words from a text
def rm_un_words_t(text, uninteresting_words):
    text = text.split('\n')
    l = []
    for line in text:
        line = rm_un_words_l(line, uninteresting_words)
        l.append(line)
    result = '\n'.join(l)
    return result

#calculate the frequancy of words in a text and returns it as a dictionary
def calculate_frequencies(text, words_to_not_include):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = words_to_not_include.split()
    text = remove_pun(text, punctuations)
    text = rm_un_words_t(text, uninteresting_words)
    text = text.split()
    d = {}
    for word in text:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d

def main():
    
    F1 = open(sys.argv[1], "r")
    F2 = open(sys.argv[2] , "r")
    text = F1.read()
    words_to_not_include = F2.read()
    cloud = WordCloud()
    cloud.generate_from_frequencies(calculate_frequencies(text, words_to_not_include))
    cloud.to_file("image.png")
    F1.close()
    F2.close()

if __name__ == "__main__":
    main()
