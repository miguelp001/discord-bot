import dice
from discord.ext import commands
import discord
import json

class Fate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.amounts = {}
    
    def doSave():
        with open('amounts.json', 'w+') as f:
            json.dump(self.amounts, f)

    async def on_ready():
      global amounts
      try:
          with open('amounts.json') as f:             
              amounts = json.load(f)
      except FileNotFoundError:
          print("Could not load amounts.json")
          amounts = {}
  
    @commands.command()
    async def roll(self, ctx, value):
        """Rolls a dice in NdN format."""
        try:
            result = dice.roll(value)
            await ctx.send(result)
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return
    ''' Below this is a work in progress for remembering stats.

    '''
    @commands.command(pass_context=True)
    async def balance(self, ctx):
        id = ctx.message.author.id
        if id in self.amounts:
            await ctx.send("You have {} in the bank".format(self.amounts[id]))
        else:
            await ctx.send("You do not have an account")

    @commands.command(pass_context=True)
    async def register(self, ctx):
        id = ctx.message.author.id
        if id not in self.amounts:
            self.amounts[id] = 100
            await ctx.send("You are now registered")
            self.doSave()
        else:
            await ctx.send("You already have an account")

    @commands.command(pass_context=True)
    async def transfer(ctx, amount: int, other: discord.Member):
        primary_id = ctx.message.author.id
        other_id = other.id
        if primary_id not in amounts:
            await bot.say("You do not have an account")
        elif other_id not in amounts:
            await bot.say("The other party does not have an account")
        elif amounts[primary_id] < amount:
            await bot.say("You cannot afford this transaction")
        else:
            amounts[primary_id] -= amount
            amounts[other_id] += amount
            await bot.say("Transaction complete")
        _save()

    

    @commands.command()
    async def save():
        doSave()


''' The new code ends here '''
def setup(bot):
    bot.add_cog(Fate(bot))