from redbot.core import commands

class BMICo(commands.Cog):
    """A cog for calculating Body Mass Index (BMI)."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bmi(self, ctx, height_cm: float, weight: float):
        """
        Calculate the Body Mass Index (BMI) and determine weight category.
        
        Parameters:
        height_cm: Height in centimeters.
        weight: Weight in kilograms.
        """
        if height_cm <= 0 or weight <= 0:
            await ctx.send("Please enter valid height and weight values.")
            return

        # Convert height from cm to meters
        height_m = height_cm / 100

        bmi_value = weight / (height_m ** 2)

        # Determine BMI category
        if bmi_value < 18.5:
            category = "underweight"
        elif 18.5 <= bmi_value < 25:
            category = "normal weight"
        elif 25 <= bmi_value < 30:
            category = "overweight"
        else:
            category = "obesity"

        await ctx.send(f"Your BMI is: {bmi_value:.2f}, which is {category}.")

def setup(bot):
    bot.add_cog(BMICo(bot))