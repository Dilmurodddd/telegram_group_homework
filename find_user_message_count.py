from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    dig = {}

    for x in users_id:

        s = 0

        for n in data["messages"]:

            if "actor" in n:
                if n["actor"] == x:

                    s += 1
            else:
                if n["from"] == x:
                    s += 1

        dig[x] = s

    return dig

     


fayl = open("data/result.json").read()

data = find_user_message_count(read_data(fayl), find_all_users_id(read_data(fayl)))

print(data)