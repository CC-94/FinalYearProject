
#Assign your Genius.com credentials and select your artist
import lyricsgenius as genius
geniusCreds = "eaIZHw-d7dxFiQsoUoPyimMC3N19a_9ix8qYFmbwMZniPCNg4auwJ0lo-u6uhMs_"
artist_name = "Saweetie"
artist_name2 = "$NOT"

#Connect your credentials and chosen artist to the genius object then takes the first 40 songs
api = genius.Genius(geniusCreds)
artist = api.search_artist(artist_name, max_songs=40)
import os
os.getcwd()
artist.save_lyrics()
artist2 = api.search_artist(artist_name2, max_songs=40)
artist2.save_lyrics()