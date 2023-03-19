# Telegramm bot for OpenAI GPT 3.5 Turbo

Ready for one file pyinstaller compilation:

with separated .env settings
`pyinstaller GPT_bot_02.py --onefile  --copy-metadata magic_filter`

or if this file will be included in execution file, unlock
`#application_path = sys._MEIPASS`

`pyinstaller GPT_bot_02.py --onefile --add-data '.env;.' --copy-metadata magic_filter`
