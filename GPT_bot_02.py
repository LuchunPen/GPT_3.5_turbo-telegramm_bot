import os
import sys
import openai
import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_app_directory():
    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        #application_path = sys._MEIPASS
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    return application_path


def get_env_path():
    directory_path = get_app_directory()
    result_path = os.path.join(directory_path, '.env')
    return result_path

# Initialize bot and dispatcher
load_dotenv(get_env_path())
openai.api_key=os.getenv('OPENAI_KEY')
bot=Bot(os.getenv('TELEGRAMM_TOKEN'))
dp=Dispatcher(bot)

botRole = os.getenv('OPENAI_ROLE')
status = 0

async def ai(user_message):
    try:
        complection=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": botRole},
                {"role": "user", "content": user_message}
            ]
        )
        return complection.choices[0].message.content
    except:
        return None


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    global status
    status = 1
    if (not botRole):
        await message.reply("Chat started by default")
    else:
        await message.reply("Chat started with bot role: " + botRole)


@dp.message_handler(commands=['stop'])
async def send_welcome(message: types.Message):
    global status
    status = 0
    await message.reply("Chat stopped")


@dp.message_handler(commands=['chatrole'])
async def send_welcome(message: types.Message):
    global status
    status = 2
    await message.reply("Describe me")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("/start - start chatting\n/chatrole - describing chat role\n/stop - stop chatting")


@dp.message_handler()
async def echo(message: types.Message):
    if (status == 1):
        print("You: " + message.text)
        answer = await ai(message.text)
        if (answer != None):
            await message.answer(answer)
            print("Bot: " + answer)
        else:
            await message.reply("Cant answer, lets try to repeat later")
    elif (status == 2):
        global botRole
        botRole = message.text
        await message.reply("Applying role success: " + botRole)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)