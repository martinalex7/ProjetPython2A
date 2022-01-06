# Python for Data Scientist Project 2021-2022 : 
*"My life is all I have. 
My rhymes, my pen, my pad"* Morray, JCole, 21 Savage - My Life

During this Natural Language Processing project we decided to work on classification algorithms applied to song lyrics. 
We aimed to create a ML/DL algorithm which could recognize which artist wrote a given song thanks to the song's lyrics only.

In order to gather a consequent and relevant database, we scrapped the website https://genius.com/.

**Genius** is a music media dealing with the latest music release and news. However it is more widely known for displaying lyrics, and lyrics explanations, for almost every song ever released.


![](https://upload.wikimedia.org/wikipedia/commons/3/3d/Genius_Logo.png)


:pushpin: This project can be seen though these two following versions:

- The **"rapport" version** of the project which is the deliverable for the Python for Data Scientist project. It is structured in 3 numerated notebook located in the rapport folder.

- The **"meant to be cloned" version**, with which you'll be able to select your own artists of interest, extract their discography, and
  test the classification models we worked on.

*NB : this project was designed for english songs only.* 

## Install requirements: 
In your terminal/command-line go to the project folder and execute the command below:
```bash
pip install -r requirements.txt 
```

## Step 1 : Chose your artists

Please run the following command in your terminal and follow carefully the instructions.
```
python scrapping.py
```

You'll be asked to enter the full name of your artist of interest. ( :warning: it is important not to misspell the artist's name).

Great ! The scrapping is now over. Your data is stored in the artist_data folder. 
You've supposedly collected every lyrics ever written by your artist (according to genius).

:repeat: You can now repeat this first step with every artist of your choosing.

## Classification Methods

During our experiments, we decided to try and compare the following classification methods on both binary classes and multivariate classes.  
- Decision Tree Algorithm
- Random Forest Algorithm
- Naive Bayes Algorithm
- Support Vector Machine Algorithm

Let's first try our classification methods for *binary classes*.

## Step 2 : Preprocessing the 2 Artists Classification Methods

In order to test our different methods, we first need you to create the TF-IDF matrix for your song corpus.

Please run the following command in your terminal and follow carefully the instructions.
```
python 2ArtistsClassificationMethods/tfidf_2.py
```

You'll be asked to type the names of the two artist. :warning: Please keep the exact syntax you used in Step 1 when scrapping the data.

This step is now over, you can choose one of our 3 classification methods (our Naive Bayes experiments are only available in our rapport notebook at the moment).

## Step 3 : The 2 Artist Classification Methods

You can now choose between the **Decision Tree Method**, the **Random Forest Method** and **Support Machine Vector Method**.

:arrow_forward: In the 2ArtistsClassificationMethods/classification_methods folder, select the documents related to your method and run it.

By following carefully the instructions (:warning: and still following the same syntax for your artist names), you should now see the accuracy results of your test. 

Once you'll be done with the binary test, you can move on to multiclass classification tests.

## Step 4 : Preprocessing the N Artists Classification Methods

In order to test our different methods, we first need you to create the TF-IDF matrix for your song corpus.

Please run the following command in your terminal.
```
python NArtistsClassificationMethods/tfidf_N.py
```

This time, the TF-IDF matrix will be created for every artist you've scrapped.

## Step 5 : The Multiple Artists Classification Methods

You can now choose between the **Decision Tree Method**, the **Random Forest Method** and **Support Machine Vector Method**.

▶️In the NArtistsClassificationMethods/classification_methods folder, select the documents related to your method and run it.

By following carefully the instructions, you should now see the accuracy results of your test. 



## Annexes :  

### Methods comparison

During our trials, we collected data on the following artists: 

*Drake , Lana Del Rey, Kanye West, Bruno Mars, Adele* & *Eminem*


This table shows the accuracy scores we obtained for each method. 

The N artist tests were made on our 6 artists, while the two artists tests were on Kanye West and Drake 

|                          | Decision Tree Method | Random Forest Method | Naive Bayes | Support Vector Machine |
| :----------------------: | :------------------: | :------------------: | :---------: |:----------------------:|
| 2 Artists Classification | 0.7795               | 0.765                | 0.75        | 0.867                  |
| N Artists Classification | 0.7329               | 0.84                 | 0.275       | 0.84                   |

### Common errors resolution

⚠️According to the way you run the different files, the following errors might occur:
- in paths the one dot : './' might need to be replaced by the two dot '../' (and vice versa)
- the column containing the song ids which appear in the DataFrame because of the .reset_index() function can take the names 'level_0' or 'index'
