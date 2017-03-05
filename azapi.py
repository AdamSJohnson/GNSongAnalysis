#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       AZLyricsAPI.py, mini-API for AZLyrics
#
#       Copyright 2013 Francesco Guarneri <Black_Ram>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
import pynn
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
from urllib.error import HTTPError
import pygn
def generating(clientID='', userID='',artist='', title='', album='', save=''):
        if title is bool:
            return 0

        artist = artist.lower().replace(" ", "-")
        title = title.lower().replace(" ", "-")
        album = album.lower().replace(" ", "-")
        if artist == '':
            print('no artist name')
            temp = pygn.search(clientID=clientID, userID=userID, track=title)

            artist = temp['track_artist_name']

            #print(artist)
            #return 0
        try:
            generate_url = 'http://lyrics.az/' + artist + '/'+album+ '/' + title + '.html'
            #urllib.request.urlopen(generate_url)
            return processing(generate_url, artist, title, save)
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
    upbreak = '(adsbygoogle = window.adsbygoogle || []).push({});'
    lowbreak = 'Correct these Lyrics'
    try:
        lyrics = soup.get_text()
    except UnicodeDecodeError:
        return 0
    lyrics = lyrics.split(upbreak)[1]
    lyrics = lyrics.split(lowbreak)[0]
    #print(lyrics)


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
