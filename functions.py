import re
import nltk
from nltk.tokenize import word_tokenize

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
    lyrics = str(lyrics).replace('25EmbedShare URLCopyEmbedCopy',' ')
    return lyrics

def tokenized_lyrics(lyrics):
    # à voir comment améliorer en supprimant les stopwords + ponctuation
    return word_tokenize(str(lyrics))