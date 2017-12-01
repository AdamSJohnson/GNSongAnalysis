# Find the HTML page from Lyrics.az that contain lyrics for the given artist song and album.     #
# This is a modified version of the AZAPI                                                        #
#           Found here: https://github.com/FrancescoGuarneri/AzLyricsAPI/blob/master/api/azapi.py#
##################################################################################################
import pynn
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
from urllib.error import HTTPError
import pygn

def generating(clientID='', userID='',artist='', title='', album='', save=''):
        if title is bool:
            return 0

        #convert the three fields into usable link tokens
        artist = artist.lower().replace(" ", "-")
        title = title.lower().replace(" ", "-")
        album = album.lower().replace(" ", "-")

        #if the artis is blank we will try to find a new artist usying pygn
        if artist == '':
            print('no artist name')
            temp = pygn.search(clientID=clientID, userID=userID, track=title)

            artist = temp['track_artist_name']

            #print(artist)
            #return 0

        #lets try to lookup the lyrics sit
        try:
            generate_url = 'http://lyrics.az/' + artist + '/'+album+ '/' + title + '.html'
            #urllib.request.urlopen(generate_url)
            return processing(generate_url, artist, title, save)

        #in this case we can try the url with the '-' album
        except HTTPError:
            if album != '-':
                return generating(clientID=clientID,\
                                 userID=userID,\
                                 artist=artist,\
                                 title= title,\
                                 album='-',\
                                 save = True
                                 )
            else :
                print('failed!')
                generate_url = 'http://lyrics.az/' + artist + '/' + album + '/' + title + '.html'
                print(generate_url)
                print('-===-')
                return 0


        
def processing(generate_url, artist, title, save):
    #print(generate_url)
    first = urllib.request.Request(generate_url, headers ={'User-agent' : 'Magic Browser'})
    response = urllib.request.urlopen(first)
    read_lyrics = response.read()

    soup = BeautifulSoup(read_lyrics, "html.parser")
    upbreak = 'LYRICS.AZ APPLICATION'
    lowbreak = 'Correct these Lyrics'
    try:
        lyrics = soup.get_text()
    except UnicodeDecodeError:
        return 0
    lyrics = lyrics.split(upbreak)[1]
    lyrics = lyrics.split(lowbreak)[0]
    print(lyrics)


    return printing(artist, title, save, lyrics)

    
def printing(artist, title, save, lyrics):    
    #for x in lyrics:
    #    print(x, end="\n\n")
    if save == True:
        return saving(artist, title, lyrics)
    elif save == False:
        pass
            
def saving(artist, title, lyrics):
    f = open(artist + '_' + title + '.txt', 'w')
    try:
        f.write(lyrics)
        f.close()
        return artist + '_' + title + '.txt'
    except UnicodeEncodeError:
        f.close()
        pynn.analyze().teardown(artist + '_' + title + '.txt')
        return 0
