
#Assign your Genius.com credentials and select your artist
import lyricsgenius as genius
geniusCreds = "eaIZHw-d7dxFiQsoUoPyimMC3N19a_9ix8qYFmbwMZniPCNg4auwJ0lo-u6uhMs_"
artist_name = "Pentatonix"
artist_name1 = "Kesha"
artist_name2 = "Ellie Goulding"
artist_name3 = "Calvin Harris"
artist_name4 = "David Guetta"
artist_name5 = "The Lumineers"
artist_name6 = "Train"
artist_name7 = "Trey Songz"
artist_name8 = "Demi Lovato"
artist_name9 = "Panic! At The Disco"
artist_name10 = "John Legend"

api = genius.Genius(geniusCreds)
import os
os.getcwd()
artist = api.search_artist(artist_name, max_songs=40)
artist.save_lyrics()
artist1 = api.search_artist(artist_name1, max_songs=40)
artist1.save_lyrics()
artist2 = api.search_artist(artist_name2, max_songs=40)
artist2.save_lyrics()
artist3 = api.search_artist(artist_name3, max_songs=40)
artist3.save_lyrics()
artist4 = api.search_artist(artist_name4, max_songs=40)
artist4.save_lyrics()
artist5 = api.search_artist(artist_name5, max_songs=40)
artist5.save_lyrics()
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