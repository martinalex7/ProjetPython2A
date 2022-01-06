import re
import numpy as np
import nltk
from nltk import word_tokenize
from lyricsgenius import Genius
import collections
from nltk.stem import WordNetLemmatizer
#nltk.download('omw-1.4')
WNL = WordNetLemmatizer()


def lyrics_for_df(id_):
    return Genius.lyrics(song_id=id_)

#
def intro_detection(lyrics):
    regex_indications = re.compile('\[(.*?)\]')
    details = [i[0] for i in regex_indications.finditer(str(lyrics))]
    for element in details:
        if 'Intro' in element:
            return 1
    return 0

def outro_detection(lyrics):
    regex_indications = re.compile('\[(.*?)\]')
    details = [i[0] for i in regex_indications.finditer(str(lyrics))]
    for element in details:
        if 'Outro' in element:
            return 1
    return 0

def nbr_verses(lyrics):
    compteur = 0
    regex_indications = re.compile('\[(.*?)\]')
    details = [i[0] for i in regex_indications.finditer(str(lyrics))]
    for element in details:
        #print(element)
        if 'Verse' in element:
            compteur +=1
    return compteur

def nbr_chorus(lyrics):
    compteur = 0
    regex_indications = re.compile('\[(.*?)\]')
    details = [i[0] for i in regex_indications.finditer(str(lyrics))]
    for element in details:
        #print(element)
        if 'Chorus' in element:
            if not 'Pre-Chorus' in element:
                compteur +=1
        if 'Refrain' in element:
            compteur +=1
    return compteur

def nbr_parts(lyrics):
    compteur = 0
    regex_indications = re.compile('\[(.*?)\]')
    details = [i[0] for i in regex_indications.finditer(str(lyrics))]
    for element in details:
        #print(element)
        if 'Part' in element:
            compteur +=1
    return compteur

def nbr_interlude(lyrics):
    compteur = 0
    regex_indications = re.compile('\[(.*?)\]')
    details = [i[0] for i in regex_indications.finditer(str(lyrics))]
    for element in details:
        #print(element)
        if 'Interlude' in element:
            compteur +=1
    return compteur

def nbr_bridge(lyrics):
    compteur = 0
    regex_indications = re.compile('\[(.*?)\]')
    details = [i[0] for i in regex_indications.finditer(str(lyrics))]
    for element in details:
        #print(element)
        if 'Bridge' in element:
            compteur +=1
    return compteur

def nbr_pre_chorus(lyrics):
    compteur = 0
    regex_indications = re.compile('\[(.*?)\]')
    details = [i[0] for i in regex_indications.finditer(str(lyrics))]
    for element in details:
        #print(element)
        if 'Pre-Chorus' in element:
            compteur +=1
    return compteur



def lyrics_cleaning(lyrics):
    regex_indications = re.compile('\[(.*?)\]')
    details = [i[0] for i in regex_indications.finditer(str(lyrics))]
    for element in details:
        lyrics = str(lyrics).replace(element,' ')
    lyrics = str(lyrics).replace('\n',' ')
    lyrics = str(lyrics).replace('\'',' ')
    lyrics = str(lyrics).replace('25EmbedShare',' ')
    lyrics = str(lyrics).replace('URLCopyEmbedCopy',' ')
    lyrics = ' '.join(smallest_lemma(WNL.lemmatize(word.lower()),
                                     WNL.lemmatize(word.lower(),pos='v')) for word in word_tokenize(str(lyrics)) if word.isalpha())
    return str(lyrics)

def tokenized_lyrics(lyrics):
    # à voir comment améliorer en supprimant les stopwords + ponctuation
    return word_tokenize(str(lyrics))


def smallest_lemma(word1,word2):
    if len(word1) >= len(word2):
        return word2
    else:
        return word1

def date_sortie(date):
    return date['year']


def dict_freq_words(tok_lyrics):
    return dict(sorted(collections.Counter(tok_lyrics).items(), key = lambda item : item[1], reverse = True))

def featuring(vec):
    col1,col2 = vec[0],vec[1]
    if col1 == col2:
        return 0
    else:
        return 1

def len_song(tok_lyrics):
    return len(tok_lyrics)

