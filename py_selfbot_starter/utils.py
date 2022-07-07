import datetime
import random
import discord
import asyncio


def message_logger(func):
    async def wrapper(self, message, *args, **kwargs):

        await func(self, message, *args, **kwargs)
        print(
            f"{self.user} ({datetime.now().strftime('%d/%m/%y, %I:%M:%S %p')}): {message}"
        )
        return

    return wrapper


@message_logger
async def send_message(self, message: str, channel=0, *args, **kwargs):
    if channel == 0:
        channel = self.channel
    await self.get_channel(channel).send(message)


async def click_button(
    self, message: discord.Message, index=None, retries=4, *args, **kwargs
):
    if len(message.components) == 0:
        return

    cmp_idx = 0
    if index:
        cmp_idx = index // 5
        index %= 5
    number_of_buttons = len(message.components[cmp_idx].children)

    if index == None:
        index = random.randrange(0, number_of_buttons)

    retry = 0
    while retry < retries:
        try:
            await asyncio.sleep(1)
            await message.components[cmp_idx].children[index].click()
            retry += 1
        except Exception as e:
            print(f"error: {e}")
            retry += 1
            continue
        break
