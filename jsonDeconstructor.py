import json
import os

class JSONDeconstructor:
    
        # Initialize JSONDeconstructor instance.

        # Args:
        # - data_dict (dict): Dictionary containing JSON data to deconstruct.
        # - file_path (str): Path to directory containing JSON files.
     
    def __init__(self,data_dict,file_path):
        self.data_dict = data_dict
        self.file_path = file_path
        self.json_data = None
      
        # Recursively search for a specific key in a nested dictionary/list structure.

        # Args:
        # - key (str): Key to search for in data_dict.

        # Returns:
        # - Corresponding value if found, None otherwise.
        
    def get_value(self, key):
        def recursive_search(dictionary, key):
            if isinstance(dictionary, dict):
                for k, v in dictionary.items():
                    if k == key:
                        return v
                    elif isinstance(v, (dict, list)):
                        result = recursive_search(v, key)
                        if result is not None:
                            return result
            elif isinstance(dictionary, list):
                for item in dictionary:
                    result = recursive_search(item, key)
                    if result is not None:
                        return result
            return None
        
        return recursive_search(self.data_dict, key)
     
        # Process one JSON file from the specified directory.
        # Sets json_data attribute with the loaded JSON data.
       
    def process_one_json_file(self):
        files = os.listdir(self.file_path)
        for file_name in files: 
         if file_name.endswith('.json'):
            file_path = os.path.join(self.file_path, file_name)
            
        try:
            with open(file_path, 'r') as f:    
                self.json_data = json.load(f)  # Load JSON data from file
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in file {self.file_path}: {e}")
      
   
        # Retrieve specific values ('title', 'type', 'episodes', 'status', 'rating', 'score') 
        # from the loaded JSON data using get_value method.

        # Returns:
        # - Tuple containing retrieved values.
     
    def dataCollectFromJson(self):
        
        if self.json_data is None:
             self.process_one_json_file()
     
    
        # Create an instance of JSONDeconstructor with the 'data' key from json_data filepath just place holder
             
        deconstructor = JSONDeconstructor(self.json_data['data'],self.file_path)
    
        # Retrieve specific values using the get_value method
        title = deconstructor.get_value('title')
        anime_type = deconstructor.get_value('type')
        episodes = deconstructor.get_value('episodes')
        status = deconstructor.get_value('status')
        rating = deconstructor.get_value('rating')
        score = deconstructor.get_value('score')  # Fixed missing argument

        return title, anime_type, episodes, status, rating, score
    #Enter your file path 
file_path = r'Your JsonHolder file path'
data_dict = {}
json_deconstructor = JSONDeconstructor(data_dict,file_path)
title, anime_type, episodes, status, rating, score = json_deconstructor.dataCollectFromJson()

print(f"Title: {title}, Type: {anime_type}, Episodes: {episodes}, Status: {status}, Rating: {rating}, Score: {score}")
