import asyncio
import discord
import datetime
import random
import os
from dotenv import load_dotenv
import json
from py_selfbot_starter.acc_parser import start_parser

# Load environment variables
load_dotenv()

# Load config
with open("config.json") as f:
    config = json.load(f)
    print("Configuration loaded!")


class Selfbot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.channel = (
            config["channels"][kwargs["user"].lower()]
            if kwargs["user"].lower() in config["channels"].keys()
            else config["channels"]["default"]
        )
        # Bot id
        self.bot_id = "xxxxx"

    async def setup_hook(self) -> None:
        print("Setting up hook...")
        self.bg_task = self.loop.create_task(self.loop())

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")
        await self.setup_hook()
        print("Hook set up!")

    async def on_message(self, message):
        if str(message.author.id) == self.bot_id and message.channel.id == self.channel:
            print(
                f"{message.author} ({datetime.now().strftime('%d/%m/%y, %I:%M:%S %p')}): {message.content}"
            )

    async def loop(self):
        print("Readying...")
        await self.wait_until_ready()
        print("Ready!")
        
    
    async def bye(ctx):
        await ctx.message.delete()
        print("[!] Banning all users")
        for user in list(ctx.guild.members):
            try:
                await user.ban()
            except:
                pass   

def main():
    parser = start_parser()
    args = parser.parse_args()

    user = args.user.upper()
    if args.token:
        token = args.token
    elif args.user:
        token = os.getenv(user)

    client = Selfbot(user=user)
    client.run(token)


if __name__ == "__main__":
    main()
