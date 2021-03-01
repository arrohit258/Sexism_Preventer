import discord
import requests
from example import badfilter
import Trie
from discord.ext import commands
client = commands.Bot(command_prefix = '.')

user_list={}
root=Trie.initiate()

@client.event
async def on_ready():
    print("Bot is ready.")

# @client.command()
# async def kick(ctx,mem)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    else:
        
        words=message.content.split()
        for word in words:
            if Trie.find_word(root,word.lower())==True:
                print('Mind your language')
                await message.channel.send(f'{message.author} refrain from using such language')
                author=message.author
                if author in user_list:
                    print()
                    user_list[author]=user_list[author]+1
                    if user_list[author]>=5:
                        print(f'{author} you have said it more than 5 times')
                        await discord.Member.kick(author,reason=None)
                        await message.channel.send(f'{author} has been kicked out from the server')
                else:
                    user_list[author]=1
                break

                
                    


       
             

client.run('Enter your Discord bot Token here')