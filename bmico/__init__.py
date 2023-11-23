from .bmico import BMICo

async def setup(bot):
    await bot.add_cog(BMICo(bot))