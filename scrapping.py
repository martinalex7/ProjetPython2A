from lyricsgenius import Genius
import pandas as pd

#token permettant de scrapper genius
token = 'sxXw2RwH_IyZ_AYE4gvp8Myo7sT0z8B-wEErToK43kDfEXk7pLBf0X7nfauTmh0g'

genius = Genius(token,timeout=45,retries=3)

#liste des artistes à scrapper
#artiste + artist_id permettant d'identifier l'artiste sur genius
list_artist_ids = [[72,'Kanye West']]

def lyrics_for_df(id_):
    return genius.lyrics(song_id=id_)

df_total = pd.DataFrame()

for artist_id, artist_name in list_artist_ids:

    # création d'un DF contenant les infos de l'ensemble des albums de l'artiste
    albums_artist = pd.concat([pd.DataFrame.from_dict(genius.artist_albums(artist_id=artist_id)['albums'])['name'],
                               pd.DataFrame.from_dict(genius.artist_albums(artist_id=artist_id)['albums'])['id'],
                               pd.DataFrame.from_dict(genius.artist_albums(artist_id=artist_id)['albums'])[
                                   'release_date_components']],
                              axis=1)

    albums_artist['Artiste'] = artist_name

    df_artist = pd.DataFrame()

    for album_id in albums_artist['id']:
        tracklist = pd.DataFrame([i['song'] for i in genius.album_tracks(album_id)['tracks']])

        v = pd.DataFrame(albums_artist.loc[albums_artist['id'] == album_id])
        print(v['name'].values)
        data_annexes = [v['name'].values[0], v['id'].values[0], v['release_date_components'].values[0],
                        v['Artiste'].values[0]]
        annexe = pd.DataFrame([data_annexes for i in range(len(genius.album_tracks(album_id)['tracks']))],
                              columns=["Album", "album_id", "Date de sortie", "Artiste"])

        tracklist = pd.concat([tracklist['title'], tracklist['id'], tracklist['artist_names'], annexe], axis=1)
        tracklist = tracklist.rename(columns={'title': 'Titre', 'id': 'song_id', 'artist_names': 'Artiste (features)'})

        tracklist['Lyrics'] = tracklist['song_id'].apply(lyrics_for_df)

        df_artist = pd.concat([df_artist, tracklist], axis=0)

        print(df_artist)

    df_artist.to_csv(f'scrapped_data/discography_{artist_name}')

    df_total = pd.concat([df_total, df_artist], axis=0)

df_total.to_csv('scrapped_data/fulldatabase')