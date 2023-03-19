# Telegramm bot for OpenAI GPT 3.5 Turbo

Ready for one file pyinstaller compilation:

* with separated .env file settings `pyinstaller GPT_telebot.py --onefile  --copy-metadata magic_filter`


* or if this file will be included in execution file, unlock `#application_path = sys._MEIPASS`, then
    `pyinstaller GPT_telebot.py --onefile --add-data '.env;.' --copy-metadata magic_filter`
