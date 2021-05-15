
#Assign your Genius.com credentials and select your artist
import lyricsgenius as genius
geniusCreds = "eaIZHw-d7dxFiQsoUoPyimMC3N19a_9ix8qYFmbwMZniPCNg4auwJ0lo-u6uhMs_"
artist_name = "Coi Leray"

api = genius.Genius(geniusCreds)
import os
os.getcwd()
artist = api.search_artist(artist_name, max_songs=40)
artist.save_lyrics()