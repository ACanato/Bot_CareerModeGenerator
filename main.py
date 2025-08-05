import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

client = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)

@client.event
async def on_ready():
    print(f'The "{client.user}" is ready to use!')

@client.command()
async def generate(ctx):
    await ctx.message.delete()

    embed = discord.Embed(title="🎲 Choice Game to Generate Ideas", description="⚽️ EA FC (FIFA) \n 💻 Football Manager", color=discord.Color.blue())
    embed.set_footer(text="Created by: .swible (Canato)")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("⚽")
    await msg.add_reaction("💻")

ideias_fifa = [
    "Choose clubs that do not exceed 3rd to 6th place (Braga, Athletic Bilbao, Newcastle, RB Leipzig, Bergamo Calcio) and try to win the championship",
    "Sign only free transfer players",
    "A small football club was bought by a billionaire and tries to get promoted to the first division making only realistic signings",
    "Start in the lowest division of a club and try to realistically get promoted",
    "Sign lots of unknown young talents!",
    "Choose a mid-table club and remove the entire transfer budget!"
]

ideias_fm = [
    "Take a team with history from the lowest division and bring them back to the first division!",
    "Try to revolutionize the Japanese / South Korean / Indian League",
    "Start unemployed and begin from the bottom and try to develop!",
    "Sign players based on their real-life football performance",
    "Sign players only from the same country!",
    "Choose a club on the brink of bankruptcy and try to rebuild it",
    "Start at your favourite club",
    "Try to play as realistically as possible"
]

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return

    if reaction.message.author != client.user:
        return

    await reaction.message.delete()

    if reaction.emoji == "⚽":
        frase = random.choice(ideias_fifa)
        novo_embed = discord.Embed(
            title="EA FC (FIFA)",
            description=frase,
            color=discord.Color.green()
        )
    elif reaction.emoji == "💻":
        frase = random.choice(ideias_fm)
        novo_embed = discord.Embed(
            title="Football Manager (FM)",
            description=frase,
            color=discord.Color.purple()
        )
    else:
        return

    await reaction.message.channel.send(embed=novo_embed)

client.run(TOKEN)