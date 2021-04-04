import json
import requests

def format_json(token, guild_id):

    url = 'https://discord.com/api/v6/guilds/' + guild_id + '/emojis'
    headers = {"Authorization": token}
    r = requests.get(url, headers=headers)

    if r.status_code == 200: pass
    else: print('Error:' + str(r.status_code)), exit()

    data = json.loads(r.text)
    
    for x in data:
        keys_to_remove = ('roles', 'require_colons', 'managed', 'available')
        for k in keys_to_remove: x.pop(k, None)
        if 'user' in x: x.pop('user')

        x['url'] = 'https://cdn.discordapp.com/emojis/' + x.pop('id')

        if x["animated"]: x["url"] += ".gif"
        else: x["url"] += ".png"
        
        x.pop('animated')

    print('Total Emotes: ' + str(len(data)))

    name = input('\nPlease enter a emote pack name: ')
    prepend_dict = {'name':'', 'author':'Discord', 'emotes':''}

    if len(data) > 50:
        chunks = [data[x:x+50] for x in range(0, len(data), 50)]

        for i in range(0, len(chunks)):
            file_name = name + '_' + str(i+1) + '.json'
            prepend_dict['emotes'] = chunks[i]
            prepend_dict['name'] = name + '_' + str(i+1)

            with open(file_name, 'w') as file:
                json.dump(prepend_dict, file, indent=4)
            file.close()

            print('Part',str(i+1),'completed.')
        print('Success!')

    else:
        file_name2 = name + '.json'
        prepend_dict['name'] = name
        prepend_dict['emotes'] = data
        with open(file_name2, 'w') as file:
            json.dump(prepend_dict, file, indent=4)
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
    return

class main():
    from sys import version_info

    if version_info[0] < 3:
        print('This script requires Python 3 or higher')
        exit()
    
    token = input('Enter your Discord Token: ')
    
    while True:
        guild_id = str(input("Enter discord guild IDs, seperated by commas [Type '?' For a list of Servers IDs]: "))
        if guild_id == '?': list_guild_ids(token)
        else: break

    guild_id_list = list()
    guild_ids = guild_id.split(',')
    for i in guild_ids: guild_id_list.append(str(i))

    count = 0
    print('You Have entered',len(guild_id_list),'server(s)')

    for i in guild_id_list:
        print('\nServer #: ' + str(count + 1))
        format_json(token, i)
        count += 1
    exit()
