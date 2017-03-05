'''
RunThis.py is the main runner for the program. This program should open up the GUI
and allow you to use the pynn network.

'''
import pynn as pn
import pygn

import sys, pygn, json
import azapi


clientID = '752404744-E74F3C84FB5730224773813C118C14ED' # Enter your Client ID from developer.gracenote.com here
userID = pygn.register(clientID)

class __run__():

    #testing the creation and deletion of a file
    def file_create_and_delete(self):
        #make a file
        analyzer = pn.analyze()
        a , fname = analyzer.setup_analysis('R Kelly', 'Ignition')
        analyzer.teardown(fname)


    def large_scale_test(self):
        #query the grace note database and grab a list of songs and artists
        intensities = {}

        # get ourselves a radio with a bunch of songs
        result = pygn.createRadio(clientID=clientID, userID=userID, mood='42958', popularity='1000', similarity='1000')
        #print(json.dumps(result, sort_keys=True, indent=4))
        #for data in result:
        #    print('{}\n{}'.format(data['track_title'], data['track_artist_name']))

        print('GOGO AZ LYRICS')
        for data in result:
            #grab the title
            title = data['track_title']
            #grab artist name
            artist = data['track_artist_name']
            #make a tuple
            temp = [title, artist]
            #get the intensity
            intensity, fname = pn.analyze().setup_analysis(artist, title)
            #teardown the file
            pn.analyze().teardown(fname)
            #add our entry to the map
            intensities = intensities + {temp : intensity}
        for item in intensities:
            #prin the tuple
            print(item)

__run__().large_scale_test()