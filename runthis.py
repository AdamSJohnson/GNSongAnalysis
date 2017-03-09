'''
RunThis.py is the main runner for the program. This program should open up the GUI
and allow you to use the pynn network.

'''
import pynn as pn
import pygn
import sys, pygn, json
import azapi
import urllib.request, urllib.error, urllib.parse
import spotipy
from urllib.error import HTTPError

clientID = '752404744-E74F3C84FB5730224773813C118C14ED' # Enter your Client ID from developer.gracenote.com here
userID = pygn.register(clientID)

spotify = spotipy.Spotify()


class __run__():

    #testing the creation and deletion of a file
    def file_create_and_delete(self):
        #make a file
        analyzer = pn.analyze()
        a , fname = analyzer.setup_analysis('R Kelly', 'Ignition')
        analyzer.teardown(fname)


    def large_scale_test(self, _title='', _artist='',  _mood='', _genre='', _era=''):
        #query the grace note database and grab a list of songs and artists
        intensities = dict()

        # get ourselves a radio with a bunch of songs
        result = pygn.createRadio(clientID=clientID, userID=userID, \
                                  artist=_artist,\
                                  track=_title,\
                                  genre=_genre,\
                                  mood=_mood,\
                                  era=_era,
                                  )
        #print(json.dumps(result, sort_keys=True, indent=4))
        #for data in result:
        #    print('{}\n{}'.format(data['track_title'], data['track_artist_name']))

        resultAlt = pygn.search(clientID=clientID, userID=userID, track=_title, artist= _artist)
        #print (resultAlt)

        if resultAlt:
            #print(resultAlt)

            # grab the title
            title = resultAlt['track_title']
            # grab artist name
            artist = resultAlt['album_artist_name']

            # grab the album name
            album = resultAlt['album_title']
            # print(album)
            # cleaned_artists = pn.analyze().remove_accents(artist)
            cleaned_artists = pn.analyze().cleanse(artist)
            cleaned_artists = pn.analyze().remove_feat(cleaned_artists)
            cleaned_artists = pn.analyze().cleanse(cleaned_artists)

            # cleaned_title = pn.analyze().remove_accents(title)
            cleaned_title = pn.analyze().cleanse(title)
            cleaned_title = pn.analyze().remove_feat(cleaned_title)
            cleaned_title = pn.analyze().cleanse(cleaned_title)

            cleaned_album = pn.analyze().cleanse(album)
            cleaned_album = pn.analyze().remove_feat(cleaned_album)
            cleaned_album = pn.analyze().cleanse(cleaned_album)

            # make a tuple
            temp = [title, artist]
            # get the intensity

            intensity, fname = pn.analyze().setup_analysis(clientID=clientID, userID=userID,
                                                           _artist_name=cleaned_artists, _song_name=cleaned_title,
                                                           _album_title=cleaned_album)
            if intensity != 0:

                if fname != 0:
                    pn.analyze().teardown(fname)
                    # add our entry to the map
                    intensities[temp[0]] = [intensity, temp[1]]
                    print("added")

        print('GOGO AZ LYRICS')
        for data in result:
            #(result)
            if not data:
                print('No results')
                continue
            #grab the title
            title = data['track_title']
            #grab artist name
            artist = data['album_artist_name']

            #grab the album name
            album = data['album_title']
            #print(album)
            #cleaned_artists = pn.analyze().remove_accents(artist)
            cleaned_artists = pn.analyze().cleanse(artist)
            cleaned_artists = pn.analyze().remove_feat(cleaned_artists)
            cleaned_artists = pn.analyze().cleanse(cleaned_artists)

            #cleaned_title = pn.analyze().remove_accents(title)
            cleaned_title = pn.analyze().cleanse(title)
            cleaned_title = pn.analyze().remove_feat(cleaned_title)
            cleaned_title = pn.analyze().cleanse(cleaned_title)

            cleaned_album = pn.analyze().cleanse(album)
            cleaned_album = pn.analyze().remove_feat(cleaned_album)
            cleaned_album = pn.analyze().cleanse(cleaned_album)

            #make a tuple
            temp = [title, artist]
            #get the intensity

            intensity, fname = pn.analyze().setup_analysis(clientID=clientID, userID=userID, _artist_name=cleaned_artists, _song_name=cleaned_title, _album_title=cleaned_album)
            if intensity == 0:
                continue
            #teardown the file
            if fname != 0:
                pn.analyze().teardown(fname)
            #add our entry to the map
            intensities[temp[0]] = [intensity, temp[1]]
            print("added")

        for item in intensities:
            #prin the tuple

            print('{:30.30}'.format(item) +' : Compound Score ' + '{:05.2f}'.format( 100 * intensities[item][0][0]) + \
                  ' : Negative Score ' + '{:05.2f}'.format((100 * intensities[item][0][1])) + \
                  ' : Neutral Score  ' + '{:05.2f}'.format(100 * intensities[item][0][2]) + \
                  ' : Positive Score ' + '{:05.2f}'.format(100 * intensities[item][0][3]) + \
                  ' : Artist ' + '{:30.30}'.format( intensities[item][1]) + \
                  ' : Sample ' + self.link(item=item, item2=intensities[item][1]),
                  )
            self.link(item=item)

        return intensities

    def run(self, _list):
        #break down the list
        #convert 0's into ''
        useme =[]
        for x in _list:
            useme.append(str(x))


        #artist
        print(_list)
        return __run__().large_scale_test(_artist = _list[0],\
                                   _title= _list[1],\
                                   _genre= _list[2],\
                                   _mood= _list[3],\
                                   _era= _list[4],)
    def link(self, item='', item2=''):
        if not item:
            return 'no link'
        try:
            results = spotify.search(q='artist:' + item2 + ' track:' + item, type='track')
        except json.decoder.JSONDecodeError:
            return 'No link found'
        items = results['tracks']['items']
        if len(items) > 0:
            artist = items[0]
            return artist['preview_url']


#__run__().run(['Pierce the veil','','','',''])
