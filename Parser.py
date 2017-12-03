from bs4 import BeautifulSoup
import requests

#import pymongo
#client = pymongo.MongoClient("mongodb://HarryTranscripts:TranscriptsPotter@saab.ischool.utexas.edu:22")
#db = pymongo.MongoClient['HarryPotterTranscripts']
#collection = db['nimish']

import pandas as pd
import numpy as np

url = "http://transcripts.wikia.com/wiki/Harry_Potter_and_the_Philosopher%27s_Stone"
request_url  = requests.get(url)
data = request_url.text
soup = BeautifulSoup(data)

paragraph = str(soup.find_all("p"))	#select all text based on the <p> tag
paragraph = paragraph.split('<p>')    #split all <p> tags

scene_sequence = 0  #initialize scene_sequence and sequence variables
sequence = 0

#for count in range(1,10):
for count in range(1,len(paragraph)):
    scene = ''#reset variables to null for every occurence in the loop
    character = ''
    description = ''
    text = ''

    if 'Scene:' in paragraph[count]: #if "Scene:" is found, store that paragraph
        scene = paragraph[count].split(':')[1]
        scene = scene.split('<')[0] # remove html \n and </p> tags from description
        scene_sequence = scene_sequence + 1
        sequence = 0
        
    elif '<b>' in paragraph[count]:
        scene = paragraph[count]
        scene_sequence = scene_sequence + 1
        sequence = 0
        
    elif ':' in paragraph[count]:   
        text = paragraph[count].split(':')[1]
        text = text.split('\\')[0] # remove html \n and </p> tags from lines
        character = paragraph[count].split(':')[0]
        character = character.split('(')[0] # remove descriptions from character name
        sequence = sequence + 1

#Code to split lines
#        if '{' in text and '}' in text:
#            buffer_text = text
#            buffer_description = buffer_text.split('{')[0]
#            print('************')
#            print(buffer_description)
#            buffer_description = buffer_text.split('{')[1]
#            buffer_description2 = buffer_description.split('}')[0]
#            text = buffer_description.split('}')[1]
#            print('************')
#            print(buffer_description2)   
            
    elif '{' in paragraph[count] and '}' in paragraph[count]:    
        description = paragraph[count]
        sequence = sequence + 1
   
    elif '(' in paragraph[count] and ')' in paragraph[count]:
        buffer_desc = paragraph[count].split('(')[1] #removing the "(" and ")"
        description = buffer_desc.split(')')[0]
        if '<i>' in description:
            buffer_desc = buffer_desc.split('<i>')[1]
            description = buffer_desc.split('</i>')[0]
            sequence = sequence + 1
    
#    db.createCollection("nimish")    
#    db.nimish.insert ({
#            "Title":"Harry Potter test data",
#            "Series":1,
#            "Sequence":1,
#            "Contents": [{
     #               "Sequence":sequence,
#                    "Description":description,
#                    "Lines":text,
#                    "Character":character
#                    }]
#            })

            
    # insert mongoDB code here
    
    print('---------' + 'scene' + '---------')    
    print(scene)        
    
    print('---------' + 'description' + '---------')    
    print(description)
    


    print('---------' + 'character' + '---------')     
    print(character)
    
    print('---------' + 'Line' + '---------')       
    print(line)
    
    print('---------' + 'scene sequence' + '---------')  
    print(scene_sequence)
    
    print('---------' + 'sequence' + '---------')
    print(sequence)


