from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

artist1 = input('Name of the first artist: ')
artist2 = input('Name of the second artist: ')

df_artist1 = pd.read_csv(f'../artist_data/discography_{artist1}')
df_artist2 = pd.read_csv(f'../artist_data/discography_{artist2}')

df_artist1 = df_artist1[df_artist1['Clean Lyrics'].notna()]
df_artist2 = df_artist2[df_artist2['Clean Lyrics'].notna()]

# Apply TF-IDF to the data
vectorizer = TfidfVectorizer()
print(list(df_artist1['Clean Lyrics'])+list(df_artist2['Clean Lyrics']))
vectors = vectorizer.fit_transform(list(df_artist1['Clean Lyrics'])+list(df_artist2['Clean Lyrics']))
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()

# Create and store the TF-IDF matrix
tf_idf = pd.DataFrame(denselist, columns=feature_names,
                                 index=list(df_artist1['song_id'])+list(df_artist2['song_id'])).reset_index()


def artist1_indicator(index):
    for id_ in df_artist1['song_id']:
        if index == id_:
            return 1
    return 0

tf_idf['Target'] = tf_idf['index'].apply(artist1_indicator)

tf_idf.to_csv(f'tfidf_data/tfidf_{artist1}_{artist2}')