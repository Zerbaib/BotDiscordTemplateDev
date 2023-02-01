###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

# importing the required modules
import disnake
from disnake.ext import commands
import os
import asyncio
import config
from helpers import errors


class tickets(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.tickets = []

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded Cog Tickets')

    # Slash command for tickets which has options of opening a ticket, closing a ticket, and deleting a ticket

    @commands.slash_command()
    async def ticket(
        self,
        inter: disnake.ApplicationCommandInteraction,
        action: str = commands.Param(choices=["open", "close", "add", "remove"]),
        user: disnake.User = commands.Param(None, description="The user you want to add to the ticket")
    ):
        try:
            # If the user selects open, it will create a ticket
            if action == "open":
                if inter.author.id in self.tickets:
                    if _channel := disnake.utils.get(
                        inter.guild.text_channels,
                        name=f"ticket-{inter.author.name}",
                    ):
                        embed = disnake.Embed(description=f"You already have a ticket opened. {_channel.mention}")
                    else:
                        embed = disnake.Embed(description="You already have a ticket opened.")
                    return await inter.send(embed=embed, delete_after=10.0)

                # Creates a ticket category if it doesn't exist
                if not disnake.utils.get(inter.guild.categories, name="Tickets"):
                    await inter.guild.create_category("Tickets")

                # Creates the ticket channel
                channel = await inter.guild.create_text_channel(
                    name=f"ticket-{inter.author.name}",
                    category=disnake.utils.get(inter.guild.categories, name="Tickets"),
                    topic=f"Ticket created by {inter.author.name} | {inter.author.id} Time Created: {inter.created_at}",
                    reason=f"Ticket created by {inter.author.name}",
                )
                self.tickets.append(inter.author.id)
                # Sets the permissions for the ticket channel
                await channel.set_permissions(inter.author, send_messages=True, read_messages=True)
                await channel.set_permissions(inter.guild.default_role, send_messages=False, read_messages=False)

                # Sends a message to the ticket channel
                embed = disnake.Embed(title=f'Welcome to {inter.guild.name}, How may we help you?', description=f'Thank you for contacting {inter.guild.name}\'s support. Please list your issue or concerns while you wait for staff to come assist you today!')
                embed.set_footer(text=f'Command executed by {inter.author}', icon_url=inter.author.avatar.url)
                embed.set_thumbnail(url=inter.author.avatar.url)
                await channel.send(embed=embed)
                await channel.send(f'{inter.author.mention}', delete_after=0.1)

                # Sends a message to the user
                embed = disnake.Embed(title='Ticket Created', description=f"Your ticket has been created at {channel.mention} \n Please go to your ticket and list your issues / concerns", color=0x00FF00)
                embed.set_footer(text=f'Command executed by {inter.author}', icon_url=inter.author.avatar.url)
                embed.set_thumbnail(url=inter.author.avatar.url)
                await inter.response.send_message(embed=embed, ephemeral=True)

            elif action == "close":
                channel = disnake.utils.get(
                    inter.guild.channels, name=f"ticket-{inter.author.name}")
                if inter.channel.name.startswith("ticket-"):
                    await inter.channel.delete()
                    await inter.response.send_message("Your ticket has been closed.")
                else:
                    await inter.response.send_message("You don't have a ticket open.")

            elif action == "add":
                channel = disnake.utils.get(
                    inter.guild.channels, name=f"ticket-{inter.author.name}")
                if inter.channel.name.startswith("ticket-"):
                    await channel.set_permissions(inter.user, send_messages=True, read_messages=True)
                    await inter.response.send_message(f"{user.mention} has been added to the ticket.")
                else:
                    await inter.response.send_message("You don't have a ticket open.")

            elif action == "remove":
                if inter.channel.name.startswith("ticket-"):
                    await inter.channel.set_permissions(user, send_messages=False, read_messages=False)
                    await inter.response.send_message(f"{user.mention} has been removed from the ticket.")
                else:
                    await inter.response.send_message("You don't have a ticket open.")

        except Exception as e:
            print(f'Error in ticket: {e}')


def setup(bot):
    bot.add_cog(tickets(bot))
