import requests



print("  ____              _               _       _  ")               
print(" |  _ \            | |             | |     (_) ")               
print(" | |_) | __ _ _ __ | | _____       | | ___  _ _ __   ___ _ __ ")
print(" |  _ < / _` | '_ \| |/ / __|  _   | |/ _ \| | '_ \ / _ \ '__|")
print(" | |_) | (_| | | | |   <\__ \ | |__| | (_) | | | | |  __/ |   ")
print(" |____/ \__,_|_| |_|_|\_\___/  \____/ \___/|_|_| |_|\___|_|   ")
                                                              
print("                                      Made by Banks#6485")

link = input('Copy Discord invite link here: ')
if len(link) > 6:
    link = link[19:]
apilink = "https://discordapp.com/api/v6/invite/" + str(link)

print (link)

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            requests.post(apilink, headers=headers)
        print ("All Tokens Joined!")
