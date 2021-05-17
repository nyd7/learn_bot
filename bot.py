import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print('Вызван /start')
    #print(update)
    #print(1/0)
    update.message.reply_text('Привет, пользователь! Ты зачем нажал /start?')

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    #mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", use_context=True)
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    #При использовании MessageHandler укажем, 
    # что мы хотим реагировать только на текстовые сообщения - Filters.text
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    #Залогируем в файл информацию о старте бота
    logging.info("Бот стартовал")
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

if __name__== '__main__':
    main()