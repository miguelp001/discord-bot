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

def setup(bot):
    bot.add_cog(Fate(bot))