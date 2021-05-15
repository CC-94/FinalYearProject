
#Assign your Genius.com credentials and select your artist
import lyricsgenius as genius
geniusCreds = "eaIZHw-d7dxFiQsoUoPyimMC3N19a_9ix8qYFmbwMZniPCNg4auwJ0lo-u6uhMs_"
artist_name = "Tanya Tucker"
artist_name1 = "Jessie Buckley"
artist_name2 = "Eilen Jewell"
artist_name3 = "Vince Gill"
artist_name4 = "Tyler Childers"
artist_name5 = "JJ Cale"
artist_name6 = "Yola"
artist_name7 = "Kelsea Ballerini"
artist_name8 = "Ashton Lane"
artist_name9 = "Brandy Clark"
artist_name10 = "Carly Pearce"


#Connect your credentials and chosen artist to the genius object then takes the first 40 songs
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