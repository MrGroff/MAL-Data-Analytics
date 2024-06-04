import requests
import json
import time
from pathlib import Path
import sys
import re

#timer
#startTime = time.time()

#get where the program last was (this was useful for running multiple instances)
lastAnime = open("lastAnime.txt", "r")
animeStart = int(lastAnime.readline())
lastAnime.close()

#check the last anime ID and stop the program
if(sys.argv[1] == "-c"):
    print(animeStart)
    exit()

#animeList = open('animeList.txt', 'r')
######progress bar###############
import enlighten

manager = enlighten.get_manager()
pbar = manager.counter(total=int(sys.argv[1])-animeStart, desc="Downloading Annie May", unit='anime')
####################################

#loop over all anime from previous value to the user input
for i in range(animeStart,int(sys.argv[1])):
    line = "https://api.jikan.moe/v4/anime/"+str(i)+"/full" #URL for anime by ID
    anime = requests.get(line) #GET request
    if(anime.status_code == 200): #if the anime exists
        anime = anime.json()
        
        #if we fail to get the data, skip it and log the ID
        if("data" not in anime):
            log = open("log.txt", "a")
            log.write(str(i)+"\n")
            log.close()
            continue
                  
        title = anime['data']['title'] #get title
        regex = r"[\\\/\:\*\?\"\<\>\|]" #get characters that arent allowed in windows file names
        title = re.sub(regex, '', title) #remove characters that arent allowed in windows file names
        title = "dataFolder/"+title+".json" #put them in the correct folder and create the file
        
        path = Path(title) #set the path
        if(path.exists() == False): #if it exists just ignore it (we will be changing this when we write an updater tool)
            print(anime['data']['title']) #print the title to the console so we know it was added
            #write to file
            with open(title, 'w') as f: 
                json.dump(anime, f)
        #else:
            #print("Exists already")
            
    time.sleep(0.2) #so we dont get timed out
    #so if mal crashes or internet dies we know where we last were
    lastAnime = open("lastAnime.txt", "w")
    lastAnime.write(str(i))
    lastAnime.close()

    pbar.update() #progress bar
   

#timer
#endTime = time.time()
#elapsedTime = endTime - startTime
#print("Elapsed Time = %s" % elapsedTime)