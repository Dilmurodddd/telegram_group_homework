import json

def read_data(data: str) -> dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    #open file
    return json.loads(data)



# fayl = open("data/result.json").read()

# data = read_data(fayl)

# print(data)