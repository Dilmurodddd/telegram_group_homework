from read_data import read_data


def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    lis = []

    for x in data["messages"]:
        
        if "from" in x:

            lis.append(x["from"])
        else:
            lis.append(x["actor"])
    
    return lis


# fayl = open("data/result.json").read()

# g = find_all_users_id(read_data(fayl))

# print(g)