###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

# imports and stuff
import disnake
from disnake.ext import commands
import os
import random
import aiohttp
import config
from helpers import errors

class fun(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded Cog Fun')

    # Dice Roll Slash Command
    @commands.slash_command(name="dice", description="Roll a dice!")
    async def dice(inter):
        try:
            dice = ["assets/dice/1.png", "assets/dice/2.png", "assets/dice/3.png", "assets/dice/4.png", "assets/dice/5.png", "assets/dice/6.png"]    
            embed = disnake.Embed(title=f"Le dé est lancer !", color=disnake.Color.random())
            embed.set_image(file=disnake.File(random.choice(dice)))
            embed.set_footer(text=f'Demander par: {inter.author}', icon_url=inter.author.avatar.url)
            msg = await inter.send(embed=embed)
        except Exception as e:
            print(f'Error sending dice message: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending dice command: {e}"))

    # 8 ball command
    @commands.slash_command(name="8ball", description="Ask the 8ball a question!")
    async def eightball(inter, *, question):
        try:
            responses = ["C'est certain.", "Il en est ainsi.", "sans aucun doute.", "Oui - certainement.", "Vous pouvez vous y fier.", "À mon avis, oui.", "Très probablement.", "Perspectives favorables.", "Oui.", "Les signes indiquent que oui.", "Répondre vague, réessayer.", "Demandez à nouveau plus tard.", "Mieux vaut ne pas te le dire maintenant.", "Je ne peux pas prédire maintenant.", "Concentre-toi et demande encore.", "Ne compte pas dessus.", "Ma réponse est non.", "Mes sources disent non.", "Les perspectives ne sont pas si bonnes.", "Très douteux."]
            embed = disnake.Embed(title=f"8ball", description=f"Question: {question}\nAnswer: {random.choice(responses)}", color=disnake.Color.random())
            embed.set_footer(text=f'Demander par {inter.author}', icon_url=inter.author.avatar.url)
            await inter.send(embed=embed)
        except Exception as e:
            print(f'Error sending 8ball message: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending 8 Ball command: {e}"))
        
    # Coinflip Slash Command
    @commands.slash_command(name="coinflip", description="Flip a coin!")
    async def coinflip(inter):
        try:
            coin = ["face", "pile"]
            embed = disnake.Embed(title=f"Tu fait tourner la piece !", description=f"Le resultat est {random.choice(coin)}", color=disnake.Color.random())
            embed.set_footer(text=f'Demander par {inter.author}', icon_url=inter.author.avatar.url)
            await inter.send(embed=embed)
        except Exception as e:
            print(f'Error sending coinflip message: {e}')

    @commands.slash_command(
        name="randomfact",
        description="Get a random fact."
    )
    async def randomfact(self, inter):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://uselessfacts.jsph.pl/random.json?language=en") as request:
                    if request.status == 200:
                        data = await request.json()
                        embed = disnake.Embed(title=f"Fait aléatoire", description=data["text"], color=0xD75BF4)
                        embed.set_footer(text=f'Demander par {inter.author}', icon_url=inter.author.avatar.url)
                    else:
                        embed = disnake.Embed(
                            title="Error!",
                            description="There is something wrong with the API, please try again later",
                            color=0xE02B2B
                        )
                    await inter.send(embed=embed)
        except Exception as e:
            print(f'Error sending randomfact message: {e}')
            await ctx.send(embed=errors.create_error_embed(f"Error sending randomfact command: {e}"))
                
def setup(bot):
    bot.add_cog(fun(bot))
