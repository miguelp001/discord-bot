from discord.ext import commands
import jsonpickle, os, sys, random, discord

class WordSalad(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def randomClause(self, subject):
        # load wordSalad
        fileName = subject + '.json'
        with open(fileName, 'r') as words:
            wordSalad = jsonpickle.decode(words.read())

        # Decide how many clauses
        option = random.choice([True, False])
        
        # Generate the crazy
        if option == True:
            clause = random.choice(wordSalad['descriptor']) + ' ' + random.choice(wordSalad['subject']) + ' ' + random.choice(wordSalad['action'])
            
            sentence = clause.capitalize() + random.choice(wordSalad['punctuation'])
            return sentence
        else:
            clause = random.choice(wordSalad['descriptor']) + ' ' + random.choice(wordSalad['subject']) + ' ' + random.choice(wordSalad['action']) + ' ' + random.choice(wordSalad['conjunction']) + ' ' + random.choice(wordSalad['action'])
            
            sentence = clause.capitalize() + random.choice(wordSalad['punctuation'])
            return sentence

    @commands.command()
    async def engram(self, ctx):
        """Generate an engram."""
        subject = "destiny"
        embed = discord.Embed(title="You open the engram to recieve:", colour=discord.Colour(0x4a90e2), description=self.randomClause(subject))
        embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")

        await ctx.send(embed=embed)

    @commands.command()
    async def saycrazy(self, ctx):
        """Generate some crazytalk."""
        subject = "wordsalad"
        crazy = self.randomClause(subject)
        await ctx.send(crazy)
    
    @commands.command()
    async def talkcrazy(self, ctx):
        """Generate some crazytalk."""
        subject = "wordsalad"
        crazy = self.randomClause(subject)
        for i in range(2, 9):
            crazy = crazy + " " + self.randomClause(subject)
        await ctx.send(crazy)

def setup(bot):
    bot.add_cog(WordSalad(bot))