# Python for Data Scientist Project 2021-2022 : 
*" I bet I can recognize which artist wrote this song. I definitely recognize his style."*

During this Natural Language Processing project we decided to work on classification algorithms applied to song lyrics. 
We aimed to create a ML/DL algorithm which could recognize the artist who wrote a song given the lyrics of a particular song.

In order to gather a consequent and relevant database, we scrapped the website https://genius.com/. 

![alt text](https://upload.wikimedia.org/wikipedia/commons/5/51/Genius-logo.png){:height="50%" width="50%"}


:alarm: By following this pipeline, you'll be able to select your artists of interest, extract their discography, and 
test the classification models we worked on.

NB : this project is designed for english songs only. 

## Install requirements: 
In your terminal/command-line go to the project folder and execute the command below:
```bash
pip install -r requirements.txt 
```

## Step 1 : Choose the artists

Please execute/run the ... file.

You'll be asked to enter the full name of your artist of interest. (it is important for the name to not include any mistakes).

Great ! The scrapping is now over (your datas are now stored in scrapped_data). You've collected every lyrics ever written by your artist (according to genius).

You can now repeat this first step with every artist of your choosing. 


## Step 2 : Improve the database 

Please execute/run the ... file. 

This step is mandatory as it will take care of cleaning your data, 


## Step 3 : Preprocessing the 2 Artists Classification Methods

In order to test our different methods, we first need you to create the TF-IDF matrix for your song corpus.
(photo definition maths TF-IDF)

Please execute/run the ... file.

You'll be asked to type the names of the two artist. Please keep the exact syntax you used in Step 1 when scrapping the data.

This step is now over, you can now choose on of our 3 methods of classification.

## Step 4 : The 2 Artist Classification Methods

You can now choose between the Decision Tree Method, the Random Forest Method and ... 

Please execute/run the ... or ... or ... file in the 2ArtistClassMethods folder.


## Step 5 : Preprocessing the N Artists Classification Methods

In order to test our different methods, we first need you to create the TF-IDF matrix for your song corpus.

Please execute/run the ... file.

This time, the TF-IDF matrix will be created for every artist you've scrapped.

## Step 6 : The Multiple Artists Classification Methods

You can now choose between the Decision Tree Method, the Random Forest Method and ... 

Please execute/run the ... or ... or ... file in the NArtistClassMethods folder.


## Annexe : Methods comparison 

During our trials, we collected datas on the following artists: 

Drake , Lana Del Rey, Kanye West, Bruno Mars, ...

This table shows the accuracy scores we obtained for each method.

|                          | Decision Tree Method | Random Forest Method | Naive Bayes |
| :----------------------: | :------------------: | :------------------: | :---------: |
| 2 Artists Classification | 0.9                  | 0.9                  | 0.9         |
| N Artists Classification | 0.9                  | 0.9                  | 0.9         |

