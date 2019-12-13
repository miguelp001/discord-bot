import dice
from discord.ext import commands

class Fate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def roll(self, ctx, value):
        """Rolls a dice in NdN format."""
        try:
            result = dice.roll(value)
            await ctx.send(result)
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

    #@commands.command()
    #async def newChar(self, ctx, name):
    #    """A command to create a new character."""
    #    try:
    #      player.makeCharacter(ctx, name)
    #      await ctx.send("New character " + name + " successfully created.")
    #    except exception:
    #      await ctx.send("i dun goofed!")
    #      return

def setup(bot):
    bot.add_cog(Fate(bot))