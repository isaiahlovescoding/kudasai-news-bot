import os
import datetime
import asyncio
import logging

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

import extract_news

import webserver

load_dotenv() #Extrats the environment variables

# Load the Discord bot token from environment variables
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')  # Log to file
intents = discord.Intents.default()  # Set up default Discord intents
intents.message_content = True       # Enable access to message content
intents.messages = True              # Enable message events

# Create the bot instance with command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)



# --- SCHEDULED TASK -------------------------------------------------------

# Set the hour and minute for the daily news post (24-hour format)
RUN_HOUR = 20    # 20 PM
RUN_MINUTE = 30  # :30

@tasks.loop(hours=24)
async def daily_news():
    """
    Scheduled task: Fetches and posts the latest Kudasai news links to a Discord channel once per day.
    """
    channel = bot.get_channel(984254611391127632)  # Replace with your channel ID
    if channel is None:
        logging.error("Channel not found; daily_news task exiting.")
        return

    # Send each news link with a short delay between messages
    for link in extract_news.get_all_news_kudasai(base_url='https://somoskudasai.com/noticias/'):
        await channel.send(link)
        await asyncio.sleep(2)  # Prevent rate-limiting

    # Send a summary message with today's date in a kawaii style
    today = datetime.date.today()
    await channel.send(
        f'¡Konnichiwa, minna-san! Estas fueron las noticias anime del día de hoy: '
        f'{today.strftime("%d/%m/%Y")} ᕙ(⇀‸↼‶)ᕗ ne~'
    )
    logging.info(f"Daily news sent for {today.isoformat()}")

@daily_news.before_loop
async def before_daily_news():
    """
    Waits until the bot is ready, then sleeps until the next scheduled run time.
    Ensures the daily_news task starts at the desired hour and minute.
    """
    await bot.wait_until_ready()
    now = datetime.datetime.now()
    # Compute the next target run time (today or tomorrow)
    target = now.replace(hour=RUN_HOUR, minute=RUN_MINUTE, second=0, microsecond=0)
    if now >= target:
        target += datetime.timedelta(days=1)
    wait_seconds = (target - now).total_seconds()
    logging.info(f"Waiting {wait_seconds/3600:.2f}h until first daily_news run at {target.time()}")
    await asyncio.sleep(wait_seconds)

# --- BOT EVENTS -----------------------------------------------------------

@bot.event
async def on_ready():
    """
    Event handler: Called when the bot has connected to Discord and is ready.
    Starts the daily_news loop if it isn't already running.
    """
    logging.info(f'{bot.user} está lista para dar las anime news!')
    # Start the loop if it isn't already running
    if not daily_news.is_running():
        daily_news.start()

# --- RUN ------------------------------------------------------------------

if __name__ == '__main__':
    webserver.keep_alive()
    # Start the bot and begin processing events
    bot.run(token, log_handler=handler, log_level=logging.DEBUG)

