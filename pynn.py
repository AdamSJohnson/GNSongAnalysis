import nltk
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import treebank as tb

class analyze():

    '''
    Start analyzing the words
    '''
    def setup_analysis(self):
        sentence = 'this is a sample sentence.'
        t = tb.parsed_sents(sentence)
        print(sentence)
        t.draw()

nltk.download()
a = analyze()
a.setup_analysis()