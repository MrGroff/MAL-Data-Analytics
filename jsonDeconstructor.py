import json
class JSONDeconstructor:
    def __init__(self, data_dict):
        self.data_dict = data_dict
    
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

# Example usage:
if __name__ == "__main__":
    with open('Hunter_x_Hunter.json', 'r') as f:
        json_data = json.load(f)
    
    # Create an instance of JSONDeconstructor with the 'data' key from json_data
    deconstructor = JSONDeconstructor(json_data['data'])
    
    # Retrieve specific values using the get_value method
    title = deconstructor.get_value('title')
    anime_type = deconstructor.get_value('type')
    episodes = deconstructor.get_value('episodes')
    status = deconstructor.get_value('status')
    rating = deconstructor.get_value('rating')
    score = deconstructor.get_value