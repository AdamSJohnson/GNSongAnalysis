import nltk
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import treebank as tb
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from os import path
import azapi

class analyze():

    '''
    Start analyzing the words
    '''
    def setup_analysis(self):
        #get the file name


        azapi.generating('katy perry', 'roar', True)
        fname = 'katy-perry_roar.txt'

        #veriffy we got the right name
        print(fname)

        #open the file
        file_obj = open(fname, 'r')

        #put an array of the lines in a variable
        sentences = file_obj.readlines()

        #setup an intensities array
        intensities = []

        #keep track of the lines processed
        lines = 0

        #go through an analyze each of the sentences
        for sentence in sentences:


            if sentence.startswith('['):
                #must find the second [
                loc = sentence.find(']')
                print(loc)
                print(len(sentence))
                sentence = sentence[loc : len(sentence)]

            if sentence.startswith('***'):
                continue

            if sentence == '\n':
                continue

            lines += 1
            sid = SentimentIntensityAnalyzer()
            ss = sid.polarity_scores(sentence)
            print(sentence)
            temp = []
            for k in sorted(ss):
                j = ss[k]
                temp.append(j)
            intensities.append(temp)

        total = [0.0, 0.0, 0.0, 0.0]
        for intensity in intensities:
            total[0] += intensity[0]
            total[1] += intensity[1]
            total[2] += intensity[2]
            total[3] += intensity[3]

        total[0] = total[0] / lines
        total[1] = total[1] / lines
        total[2] = total[2] / lines
        total[3] = total[3] / lines
        print(total)

a = analyze()
a.setup_analysis()