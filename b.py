import discord
from discord.ext import commands
import subprocess

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='testbot')
async def test_bot(ctx, ip_port, *args):
    # Check if the command is '!testbot'
    if ctx.invoked_with == 'testbot':
        # Construct the Golang command
        golang_command = ['go', 'run', 'a.go', f'http://{ip_port}'] + list(args)
        
        try:
            # Run the Golang command using subprocess
            result = subprocess.run(golang_command, capture_output=True, text=True, check=True)
            output = result.stdout
        except subprocess.CalledProcessError as e:
            output = e.stderr

        # Send the output to the Discord channel
        await ctx.send(f'```{output}```')


# Replace 'YOUR_DISCORD_TOKEN' with your actual Discord bot token
bot.run('MTExMjQwMDUwOTk2MjMwMTUwMQ.GN0EMn._kPhPMHqJJK5W2QvhJNEEy7Tq0C6jBo3OsNPgs')
