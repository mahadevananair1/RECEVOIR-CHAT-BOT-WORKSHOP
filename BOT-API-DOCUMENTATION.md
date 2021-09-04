Since telegram itself is open source
Pleothora of libraries are available for telegram bots API
# Python
pyTelegramBotAPI (TeleBot)
Telepot
# PHP
Telegram Bot API – PHP SDK + Laravel Integration
# Java
TelegramBots
# NodeJS
Telegram Node Bot 
# Ruby
Telegram Bot
# C#
Telegram Bot API Library

At their core, all these libraries are HTTP requests wrappers. A great deal of them is written using OOP and reflects all the Telegram Bot API data types in classes.

# We use directly via HTTPS

your-bot-token --->is got by creating a bot in telegram via botfather
These are done with GET requests
https://api.telegram.org/bot<your-bot-token>/getme --->to get details about bot
https://api.telegram.org/bot<your-bot-token>/getUpdates--->to get response update
https://api.telegram.org/bot<your-bot-token>/sendMessage?chat_id=<chat_id>&text="yourtext"--->to get response update
https://api.telegram.org/bot<your-bot-token>/sendLocation?chat_id=<chat_id>&latitude="latitude"&longitude=""--->to get response update

To send files and images we need to use POST requests
requests.post(<url>,data=data_dictionary)