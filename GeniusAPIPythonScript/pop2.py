
#Assign your Genius.com credentials and select your artist
import lyricsgenius as genius
geniusCreds = "eaIZHw-d7dxFiQsoUoPyimMC3N19a_9ix8qYFmbwMZniPCNg4auwJ0lo-u6uhMs_"

artist_name6 = "Eric Church"
artist_name7 = "fun."
artist_name8 = "Billie Eilish"
artist_name9 = "Britney Spears"
artist_name10 = "Sia"

api = genius.Genius(geniusCreds)
import os
os.getcwd()

artist6 = api.search_artist(artist_name6, max_songs=40)
artist6.save_lyrics()
artist7 = api.search_artist(artist_name7, max_songs=40)
artist7.save_lyrics()
artist8 = api.search_artist(artist_name8, max_songs=40)
artist8.save_lyrics()
artist9 = api.search_artist(artist_name9, max_songs=40)
artist9.save_lyrics()
artist10 = api.search_artist(artist_name10, max_songs=40)
artist10.save_lyrics()