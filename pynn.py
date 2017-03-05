import nltk
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import treebank as tb
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
import azapi
import re
import unicodedata
import string
class analyze():

    '''
    Start analyzing the words
    '''
    def setup_analysis(self,clientID='', userID='', _artist_name='', _song_name='', _album_title=''):
        #get the file name


        check = azapi.generating(clientID=clientID,\
                                 userID=userID,\
                                 artist=_artist_name,\
                                 title= _song_name,\
                                 album=_album_title,\
                                 save = True
                                 )
        print(check)
        if(check == 0):
            return 0, 0
        fname = _artist_name.replace(' ', '-') + '_' + _song_name.replace(' ', '-') + '.txt'

        #veriffy we got the right name
        #print(fname)
        print(fname)
        #open the file
        file_obj = open(fname.lower(), 'r')

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

                sentence = sentence[loc : len(sentence)]

            if sentence.startswith('***'):
                continue

            if sentence == '\n':
                continue

            if sentence == '﻿At the moment nobody has submitted lyrics for this song to our archive.':
                #this is a problem it means there are no lyrics to the stong
                return 0, 0

            lines += 1
            sid = SentimentIntensityAnalyzer()
            ss = sid.polarity_scores(sentence)
            #print(sentence)
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
        #print(total)



        return total , fname



    def teardown(self, file_name):
        #remove the file
        os.remove(file_name.lower())


    def cleanse(self, s):
        r = re.compile(r'[{}]+'.format(re.escape(string.punctuation)))
        ex = r.sub('', s)

        ex = re.sub('[^0-9a-zA-Z]+', ' ', s)
        #check if the last char is white space
        if len(ex) == 0:
            return ex

        if ex[(len(ex) - 1)] == ' ':
            return ex[0: len(ex) - 1]

        return ex;

    def remove_feat(self, s):
        loc = s.lower().find('feat')
        if loc > 0:
            return s[0 : loc]
        return s

    def remove_accents(self, input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])



