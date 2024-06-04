import os, json
import pandas as pd

path_to_json = 'dataFolder/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
jsons_data = pd.DataFrame(columns=['title', 'ID', 'score', 'genres'])

######progress bar###############
import enlighten

manager = enlighten.get_manager()
pbar = manager.counter(total=int(len(json_files)), desc="Parsing files", unit='files')
####################################

#this will be a dict of genres storing a pair of data
#the pair of data is (score, number_of_occurences)
genreList = {}

#adds genre, score and number of occurences to the dict
def addPairGenre(genreList, iterator):
    #if the genre is already in the list:
    if(currentGenre in genreList):
    #add the new score to the current score and add 1 to the number of occurences
        genreList[json_text['data']['genres'][iterator]['name']] = genreList.get(currentGenre)[0] + score, genreList.get(currentGenre)[1] + 1
    else:
    #otherwise we add it to the dict storing the current score and setting number of occurences to 1
        genreList[json_text['data']['genres'][iterator]['name']] = score, 1

#adds genre, score and number of occurences to the dict
def addPairTheme(genreList, iterator):
    #if the theme is already in the list:
    if(currentTheme in genreList):
    #add the new score to the current score and add 1 to the number of occurences
        genreList[json_text['data']['themes'][iterator]['name']] = genreList.get(currentTheme)[0] + score, genreList.get(currentTheme)[1] + 1
    else:
    #otherwise we add it to the dict storing the current score and setting number of occurences to 1
        genreList[json_text['data']['themes'][iterator]['name']] = score, 1
        
        
counter = 0
#iterate over all json files
for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file) #load json file
        score = json_text['data']['score'] #store the score for the anime
        
        #if theres no score, skip it
        if(score == None):
            continue
            
        iterator = 0
        #iterate over genres
        for names in json_text['data']['genres']:
            #get current genre for readability
            currentGenre = json_text['data']['genres'][iterator]['name']
            #add genre, score and increment number of occurences
            addPairGenre(genreList,iterator)
            iterator += 1
                
        #reset this to 0 for the next loop
        iterator = 0   
        #iterate over themes
        for names in json_text['data']['themes']:
            #get current theme for readability
            currentTheme = json_text['data']['themes'][iterator]['name']
            #add theme, score and increment number of occurences
            addPairTheme(genreList,iterator)
            iterator += 1
            
        pbar.update() #update progress bar
        
        
        


#this will calculate the average score
for currentGenre in genreList:
    #set the key in the dict equal to the total score divided by the number of occurences
    genreList[currentGenre] = ((genreList.get(currentGenre)[0])/(genreList.get(currentGenre)[1]))
    #print(currentGenre, ": ", ((genreList.get(currentGenre)[0])/(genreList.get(currentGenre)[1])), sep = "")
    #genreList[currentGenre] = (float((genreList.get(currentGenre)[0]))/float((genreList.get(currentGenre)[1])))
        
#sort the dict by average score
######################################################################################## 
#from https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
from collections import OrderedDict
import numpy as np
keys = list(genreList.keys())
values = list(genreList.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
#print(sorted_dict)
#######################################################################################

#print them out 1 by 1
for currentGenre in sorted_dict:
    print(currentGenre, ": ",sorted_dict.get(currentGenre), sep = "")
