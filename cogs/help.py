###############################################
#           Template made by Person0z         #
#       Help Command Made by ๖̶̶̶ζ͜͡Zerbaib     #
#           https://github.com/Zerbaib        #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

import disnake
from disnake.ext import commands
import os
import config
from helpers import errors

class help(commands.Cog):

    def __init__(self, bot):
    	self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Help')
            
    # Help Command with subcommands 
    @commands.slash_command(name='help', description='Affiche la commande d\'aide',)
    async def help(
        inter: disnake.ApplicationCommandInteraction,
        action: str = commands.Param(choices=["general", "fun", 'tickets', 'radio', 'rank', 'moderation']),
    ):
        try:
            if action == "general":
                embedVar = disnake.Embed(
                    title="Commandes général !",
                    description="Vérifiez les commandes importantes, que vous pouvez utiliser !",
                    colour=config.Success())
                embedVar.add_field(name="Bot Prefix", value="```/ + !```", inline=False)
                embedVar.add_field(name="Commande général",
                                    value=
                                        "```/ping - Voir le ping du bot```" +
                                        "```/check - Vérifier si le robot est en ligne```" +
                                        "```/userinfo - Rechercher des informations sur l’utilisateur```" +
                                        "```/serverinfo - Obtenir des informations sur le serveur```" +
                                        "```/botinfo - Obtenir des renseignements sur le robot```" +
                                        "```/invite - Obtenir le lien du bot```",
                                        inline=False)
                embedVar.set_thumbnail(
                    url="https://us-east-1.tixte.net/uploads/your-parents.wants.solutions/help.png"
                )
                await inter.response.send_message(embed=embedVar)
            if action == "moderation":
                embedVar = disnake.Embed(
                    title="Commandes de modération !",
                    description="Vérifier les commandes importantes, que vous pouvez utiliser !",
                    colour=config.Success())
                embedVar.add_field(name="Bot Prefix", value="```/ + !```", inline=False)
                embedVar.add_field(name="Commandes de modération",
                                    value=
                                        "```/slowmode - Activer le mode lent pour un canal```" +
                                        "```/lock - Verrouiller le canal de tout envoie de message```" +
                                        "```/unlock - Déverrouiller le canal de tout envoie de message```" +
                                        "```/purge - Purger (supprimer) un groupe de message```" +
                                        "```/kick - Ejecter quelqu’un du serveur```" +
                                        "```/ban - Bannir quelqu’un du serveur```" +
                                        "```/unban - Debannir quelqu’un du serveur```" +
                                        "```/nuke - Nuke un canal pour tout nouveau```",
                                        inline=False)
                embedVar.set_thumbnail(
                    url="https://us-east-1.tixte.net/uploads/your-parents.wants.solutions/help.png"
                )
                await inter.response.send_message(embed=embedVar)
            if action == "fun":
                embedVar = disnake.Embed(
                    title="Commandes de fun !",
                    description="Vérifier les commandes importantes, que vous pouvez utiliser !",
                    colour=config.Success())
                embedVar.add_field(name="Bot Prefix", value="```/ + !```", inline=False)
                embedVar.add_field(name="Commandes de fun",
                                    value=
                                    "```/dice - Jouer un dé, pour obtenir un nombre de 1-6```" +
                                    "```/8ball - Poser une question, pour obtenir une réponse \"honnête\"```" +
                                    "```/coinflip - Tirez à pile ou face !```" +
                                    "```/generate - Générer une image à partir d’un texte !```" +
                                    "```/bitcoin - Vérifier le prix actuel de BitCoin```",
                                    inline=False)
                embedVar.set_thumbnail(
                    url="https://us-east-1.tixte.net/uploads/your-parents.wants.solutions/help.png"
                )
                await inter.response.send_message(embed=embedVar)
            if action == "tickets":
                embedVar = disnake.Embed(
                    title="Commandes de ticket!",
                    description="Vérifier les commandes importantes, que vous pouvez utiliser !",
                    colour=config.Success())
                embedVar.add_field(name="Bot Prefix", value="```/ + !```", inline=False)
                embedVar.add_field(name="Commandes de ticket",
                                    value=
                                    "```/ticket - créer un ticket```" +
                                    "```/close - Fermer un billet```" +
                                    "```/add - Ajouter un utilisateur à un ticket```" +
                                    "```/remove - Supprimer un utilisateur du ticket```" +
                                    "```/list - Liste les utilisateur et rôles dans un ticket```",
                                    inline=False)
                embedVar.set_thumbnail(
                    url="https://us-east-1.tixte.net/uploads/your-parents.wants.solutions/help.png"
                )
                await inter.response.send_message(embed=embedVar)
            if action == "radio":
                embedVar = disnake.Embed(
                    title="Commandes radio !",
                    description="Vérifier les commandes importantes, que vous pouvez utiliser !",
                    colour=config.Success())
                embedVar.add_field(name="Bot Prefix", value="```/ + !```", inline=False)
                embedVar.add_field(name="Commandes radio",
                                    value=
                                    "```/radio - Démarrer une station de radio```" +
                                    "```/disconnect - Arrêter une station de radio```",
                                    inline=False)
                embedVar.set_thumbnail(
                    url="https://us-east-1.tixte.net/uploads/your-parents.wants.solutions/help.png"
                )
                await inter.response.send_message(embed=embedVar)
            if action == "rank":
                embedVar = disnake.Embed(
                    title="Level Commands!",
                    description="Check important commands, that you can use!",
                    colour=config.Success())
                embedVar.add_field(name="Bot Prefix", value="```/ + !```", inline=False)
                embedVar.add_field(name="Level Commands",
                                    value=
                                    "```/rank - See your info```" +
                                    "```/leaderboard - See the member top with bigger levels```" +
                                    "```/addlevel - Add level to a member```" +
                                    "```/removelevels - Remove levels to a member```" +
                                    "```/addxp - Add xp to a member```" +
                                    "```/remove_xp - Remove xp to a member```",
                                    inline=False)
                embedVar.set_thumbnail(
                    url="https://us-east-1.tixte.net/uploads/your-parents.wants.solutions/help.png"
                )
                await inter.response.send_message(embed=embedVar)
        except Exception as e:
            print(f'Error sending help message: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending help command: {e}"))

def setup(bot):
    bot.add_cog(help(bot))