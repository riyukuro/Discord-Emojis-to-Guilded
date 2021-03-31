import json

# Credits to https://github.com/jhsu98/ for Json-Splitter.
def json_splitter(file_name, name):
    import sys
    import os
    import math

    prepend = ('{\n    "name": "%s",\n    "author": "Discord",\n    "emotes": ') % (name)

    if sys.version_info[0] < 3:
        print('This script requires Python 3 or higher')
        exit()

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
        with open(name, 'w') as outfile:
            outfile.seek(0)
            outfile.write(prepend)
            json.dump(split_data[i], outfile, indent=4)
        with open(name, 'a') as outfile:
            outfile.write('\n}')
            
        print('Part',str(i+1),'... completed')
    os.remove(file_name)
    print('Success!')

class main():
    import requests

    token = input('Enter your Discord Token: ')
    guild_id = input('Enter the Server Guild ID: ')

    url = 'https://discord.com/api/v6/guilds/' + guild_id + '/emojis'
    headers = {"Authorization": token}
    r = requests.get(url, headers=headers)

    if r.status_code == 200: pass
    else: print('Error:' + r.status_code), exit()

    data = json.loads(r.text)
    
    for x in data:
        del x['roles']
        del x['require_colons']
        del x['managed']
        del x['available']
        x['url'] = 'https://cdn.discordapp.com/emojis/' + x.pop('id')

        if x["animated"]:
            x["url"] += ".gif"
        else:
            x["url"] += ".png"
        
        del x['animated']

    print('Total Emotes: ' + str(len(data)))

    name = input('Please enter a emote pack name: ')
    prepend = ('{\n    "name": "%s",\n    "author": "Discord",\n    "emotes": ') % (name)
    file_name = name + '.json'
    
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

    if len(data) > 50:
        json_splitter(file_name, name)
    else:
        with open(file_name, 'w') as file:
            file.seek(0)
            file.write(prepend)
            json.dump(data, file, indent=4)
        with open(file_name, 'a') as file:
            file.write('\n}')
        print('Success!')