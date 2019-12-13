from discord.ext import commands
import jsonpickle, os, sys, random

#class WordSalad(commands.Cog):
#    def __init__(self, bot):
#        self.bot = bot
#
#    def crazyClause(arg):
#        # load wordSalad
#        with open('wordsalad.json', 'r') as words:
#            wordSalad = jsonpickle.decode(words.read())
#
#        # Decide how many clauses
#        option = random.choice([True, False])
#        
#        # Generate the crazy
#        if option == True:
#            clause = random.choice(wordSalad['subject']) + ' ' + random.choice(wordSalad['predicate'])
#            sentence = clause.capitalize() + random.choice(wordSalad['punctuation'])
#            return sentence
#        else:
#            clause = random.choice(wordSalad['subject']) + ' ' +random.choice(wordSalad['predicate']) + ' ' + random.choice(wordSalad['conjunction']) + ' ' + random.choice(wordSalad['subject']) + ' ' + random.choice(wordSalad['predicate'])
#            sentence = clause.capitalize() + random.choice(wordSalad['punctuation'])
#            return sentence

#    @commands.command()
#    async def saycrazy(self, ctx):
#        """Generate some crazytalk."""
#        crazy = self.crazyClause()
#        await ctx.send(crazy)
#    
#    @commands.command()
#    async def talkcrazy(self, ctx):
#        """Generate some crazytalk."""
#        crazy = self.crazyClause()
#        for i in range(2, 9):
#            crazy = crazy + " " + self.crazyClause()
#        await ctx.send(crazy)

class WordSalad(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def randomClause(subject):
        # load wordSalad
        fileName = subject + '.json'
        with open(fileName, 'r') as words:
            wordSalad = jsonpickle.decode(words.read())

        # Decide how many clauses
        option = random.choice([True, False])
        
        # Generate the crazy
        if option == True:
            clause = random.choice(wordSalad['subject']) + ' ' + random.choice(wordSalad['predicate'])
            sentence = clause.capitalize() + random.choice(wordSalad['punctuation'])
            return sentence
        else:
            clause = random.choice(wordSalad['subject']) + ' ' +random.choice(wordSalad['predicate']) + ' ' + random.choice(wordSalad['conjunction']) + ' ' + random.choice(wordSalad['subject']) + ' ' + random.choice(wordSalad['predicate'])
            sentence = clause.capitalize() + random.choice(wordSalad['punctuation'])
            return sentence

    @commands.command()
    async def engram(self, ctx):
        """Generate an engram."""
        engram = self.randomClause(destiny)
        await ctx.send(engram)

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