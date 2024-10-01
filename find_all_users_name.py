from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    listt = []

    for x in data["messages"]:
        
        if "from" in x:
            listt.append(x["from"])
        
        else:
            listt.append(x["actor"])
    
    return listt

fayl = open("data/result.json").read()

data = find_all_users_name(read_data(fayl))

print(data)