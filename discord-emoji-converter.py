import json
import requests

# Credits to https://github.com/jhsu98/ for Json-Splitter.
def json_splitter(file_name, name):
    import os
    import math

    prepend = ('{\n    "name": "%s",\n    "author": "Discord",\n    "emotes": ') % (name)

    try:
        f = open(file_name)
        file_size = os.path.getsize(file_name)
        data = json.load(f)
        data_len = len(data)

    except:
        print('Error loading JSON file ... exiting')
        exit()

    mb_per_file = abs(float(0.0055))

    # determine number of files necessary
    num_files = math.ceil(file_size/(mb_per_file*1000000))
    print('File will be split into',num_files,'equal parts')

    # initialize 2D array
    split_data = [[] for i in range(0,num_files)]

    # determine indices of cutoffs in array
    starts = [math.floor(i * data_len/num_files) for i in range(0,num_files)]
    starts.append(data_len)

    # loop through 2D array
    for i in range(0,num_files):
        # loop through each range in array
        for n in range(starts[i],starts[i+1]):
            split_data[i].append(data[n])
        
        # create file when section is complete
        name = os.path.basename(file_name).split('.')[0] + '_' + str(i+1) + '.json'
        with open(name, 'w') as file:
            file.seek(0)
            file.write(prepend)
            json.dump(split_data[i], file, indent=4)
        with open(name, 'a') as file:
            file.write('\n}')
        print('Part',str(i+1),'... completed')
        file.close()
    f.close()
    os.remove(file_name)
    print('Success!')

def format_json(token, guild_id):

    url = 'https://discord.com/api/v6/guilds/' + guild_id + '/emojis'
    headers = {"Authorization": token}
    r = requests.get(url, headers=headers)

    if r.status_code == 200: pass
    else: print('Error:' + str(r.status_code)), exit()

    data = json.loads(r.text)
    
    for x in data:
        del x['roles'], x['require_colons'], x['managed'], x['available']
        x['url'] = 'https://cdn.discordapp.com/emojis/' + x.pop('id')

        if x["animated"]: x["url"] += ".gif"
        else: x["url"] += ".png"
        
        del x['animated']

    print('Total Emotes: ' + str(len(data)))

    name = input('\nPlease enter a emote pack name: ')
    prepend = ('{\n    "name": "%s",\n    "author": "Discord",\n    "emotes": ') % (name)
    file_name = name + '.json'
    
    if len(data) > 50:
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
        file.close()
        json_splitter(file_name, name)
    else:
        with open(file_name, 'w') as file:
            file.seek(0)
            file.write(prepend)
            json.dump(data, file, indent=4)
        with open(file_name, 'a') as file:
            file.write('\n}')
        file.close()
        print('Success!')

def list_guild_ids(token):
    url = 'https://discord.com/api/v6/users/@me/guilds'
    headers = {"Authorization": token}
    r = requests.get(url, headers=headers)

    if r.status_code == 200: pass
    else: print('Error:' + str(r.status_code)), exit()

    data = json.loads(r.text)
    for x in data:
        print(x['name'] + ', ' + x['id'])
    return(data)

class main():
    from sys import version_info

    if version_info[0] < 3:
        print('This script requires Python 3 or higher')
        exit()
    
    token = input('Enter your Discord Token: ')

    guild_id = str(input("Enter discord guild IDs, seperated by commas, here [Type '?' For a list of Servers IDs]: "))
    
    while guild_id:
        if guild_id == '?': 
            guild_id is True
            list_guild_ids(token)
            guild_id = str(input('Guild IDS HERE: '))
        else: 
            guild_id_list = list()
            guild_ids = guild_id.split(',')
            for i in guild_ids: guild_id_list.append(str(i))

        count = 0
        length = len(guild_id_list)

        for i in guild_id_list:
            print('\nServer #: ' + str(count + 1))
            format_json(token, i)
            count += 1
        while count <= length: guild_id is True, exit()
