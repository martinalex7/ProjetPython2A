from lyricsgenius import Genius
import pandas as pd
from functions import *

import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

#token allowing to scrap genius
token = 'sxXw2RwH_IyZ_AYE4gvp8Myo7sT0z8B-wEErToK43kDfEXk7pLBf0X7nfauTmh0g'

genius = Genius(token,timeout=45,retries=3)

def lyrics_for_df(id_):
    return genius.lyrics(song_id=id_)

print('-------------------------------------------------------------------')
print('Which artist do you want to scrap?')
artist_name = input("Artist name : ")
artist_id = genius.search_artists(artist_name)['sections'][0]['hits'][0]['result']['id']


# creation of a DataFrame containing data on every song of the album
albums_artist = pd.concat([pd.DataFrame.from_dict(genius.artist_albums(artist_id=artist_id)['albums'])['name'],
                           pd.DataFrame.from_dict(genius.artist_albums(artist_id=artist_id)['albums'])['id'],
                           pd.DataFrame.from_dict(genius.artist_albums(artist_id=artist_id)['albums'])
                           ['release_date_components']],
                           axis=1)

albums_artist['Artiste'] = artist_name

df_artist = pd.DataFrame()

compteur = 1

for album_id in albums_artist['id']:
    try :
        tracklist = pd.DataFrame([i['song'] for i in genius.album_tracks(album_id)['tracks']])

        v = pd.DataFrame(albums_artist.loc[albums_artist['id'] == album_id])

        print('Processing...' ,f' Album n° {compteur} / {len(albums_artist)}','|',v['name'].values[0])
        compteur += 1

        data_annexes = [v['name'].values[0], v['id'].values[0], v['release_date_components'].values[0],
                        v['Artiste'].values[0]]
        annexe = pd.DataFrame([data_annexes for i in range(len(genius.album_tracks(album_id)['tracks']))],
                              columns=["Album", "album_id", "Release Date", "Artist"])

        tracklist = pd.concat([tracklist['title'], tracklist['id'], tracklist['artist_names'], annexe], axis=1)
        tracklist = tracklist.rename(columns={'title': 'Title', 'id': 'song_id', 'artist_names': 'Featuring'})

        tracklist['Lyrics'] = tracklist['song_id'].apply(lyrics_for_df)

        df_artist = pd.concat([df_artist, tracklist], axis=0)

    except :

        print('Impossible to scrap this album')

df_artist = df_artist.dropna()


df_artist['Intro'] = df_artist['Lyrics'].apply(intro_detection)
df_artist['Interlude'] = df_artist['Lyrics'].apply(nbr_interlude)
df_artist['Chorus'] = df_artist['Lyrics'].apply(nbr_chorus)
df_artist['Bridge'] = df_artist['Lyrics'].apply(nbr_bridge)
df_artist['Pre-Chorus'] = df_artist['Lyrics'].apply(nbr_pre_chorus)
df_artist['Parts'] = df_artist['Lyrics'].apply(nbr_parts)
df_artist['Verses'] = df_artist['Lyrics'].apply(nbr_verses)
df_artist['Outro'] = df_artist['Lyrics'].apply(outro_detection)
df_artist['Clean Lyrics'] = df_artist['Lyrics'].apply(lyrics_cleaning)
df_artist['Clean Tokenized Lyrics'] = df_artist['Clean Lyrics'].apply(tokenized_lyrics)
df_artist['Word Frequency in song'] = df_artist['Clean Tokenized Lyrics'].apply(dict_freq_words)
df_artist['Release Date'] = df_artist['Release Date'].apply(release_date)
df_artist['Song Length'] = df_artist['Clean Tokenized Lyrics'].apply(len_song)
df_artist['Featuring'] = df_artist[['Featuring', 'Artist']].apply(featuring, axis=1)

df_artist.to_csv(f'artist_data/discography_{artist_name}')
