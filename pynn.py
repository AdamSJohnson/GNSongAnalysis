import nltk
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import treebank as tb
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from os import path

class analyze():

    '''
    Start analyzing the words
    '''
    def setup_analysis(self):
        fname = 'DMX_test.txt'
        print(fname)
        file_obj = open(fname, 'r')
        sentences = file_obj.readlines()
        intensities = []
        lines = 0
        for sentence in sentences:
            lines += 1
            sid = SentimentIntensityAnalyzer()
            ss = sid.polarity_scores(sentence)
            print(sentence)
            for k in sorted(ss):
                intensities.append(k)
                print('{0}: {1}, '.format(k, ss[k]), end='')
            print('\n')

a = analyze()
a.setup_analysis()