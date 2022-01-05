from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import os

list_artists = os.listdir('../artist_data/')

df_artists = pd.DataFrame()

for artist in list_artists:
    df = pd.read_csv(f'../artist_data/{artist}')
    df_artists = pd.concat([df_artists,df[df['Clean Lyrics'].notna()]], axis = 0)


# Apply TF-IDF to the data
vectorizer = TfidfVectorizer()
#print(list(df_artists['Clean Lyrics']))
vectors = vectorizer.fit_transform(list(df_artists['Clean Lyrics']))
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()

# Create and store the TF-IDF matrix
tf_idf = pd.DataFrame(denselist, columns=feature_names, index=list(df_artists['song_id'])).reset_index()

def artist_indicator(index):
    return df_artists[df_artists['song_id'] == index]['Artiste'].values[0]

tf_idf['Target'] = tf_idf['index'].apply(artist_indicator)

tf_idf.to_csv(f'tfidf_data/global_tfidf')