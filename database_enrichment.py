from functions import *
import pandas as pd

artist = input('Artiste')

improved_discography = pd.read_csv('/Users/emanieluu/Documents/pythonProject/ProjetPython2A/scrapped_data/discography_{}.csv'.format(artist))

improved_discography['Intro'] = improved_discography['Lyrics'].apply(intro_detection)
improved_discography['Interlude'] = improved_discography['Lyrics'].apply(nbr_interlude)
improved_discography['Chorus'] = improved_discography['Lyrics'].apply(nbr_chorus)
improved_discography['Bridge'] = improved_discography['Lyrics'].apply(nbr_bridge)
improved_discography['Pre-Chorus'] = improved_discography['Lyrics'].apply(nbr_pre_chorus)
improved_discography['Parts'] = improved_discography['Lyrics'].apply(nbr_parts)
improved_discography['Verses'] = improved_discography['Lyrics'].apply(nbr_verses)
improved_discography['Outro'] = improved_discography['Lyrics'].apply(outro_detection)

improved_discography['Clean Lyrics'] = improved_discography['Lyrics'].apply(lyrics_cleaning)
improved_discography['Clean Tokenized Lyrics'] = improved_discography['Clean Lyrics'].apply(tokenized_lyrics)

improved_discography.to_csv(f'completed_data/final_discography_{artist}.csv')