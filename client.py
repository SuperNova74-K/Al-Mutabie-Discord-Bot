import discord
from discord.ext import commands
from discord import app_commands 
import dotenv
import os

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("BOT IS RUNNING")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command")
    except Exception as e:
        print(e)

@bot.tree.command(name="greet")
async def greet(interaction: discord.Interaction):
    await interaction.response.send_message(f"Scream My Soldier {interaction.user.mention}", ephemeral=True)

@bot.tree.command(name="mention")
@app_commands.describe(who="who")
async def mention(interaction: discord.Interaction, who: str):
    await interaction.response.send_message(f"Hey Soldier{who}")

@bot.tree.command(name="tasks")
@app_commands.describe(who="who")
async def show_tasks(interaction: discord.Interaction, who: str, task_num: int):
    pass

@bot.tree.command(name="delete_task")
@app_commands.describe(who="who")
@app_commands.describe(task_num="task_num")
async def delete_task(interaction: discord.Interaction, who: str, task_num: int):
    await interaction.response.send_message(f"Hey Soldier {who}, You Deleted Task {task_num}")


# TODO: Get Task Instructions

def run_bot():
    dotenv.load_dotenv()
    bot.run(os.getenv("API_TOKEN"))