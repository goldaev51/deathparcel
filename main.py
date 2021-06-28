import telebot
bot = telebot.TeleBot("1813530521:AAED5rs5vGWQOsZ5mkqRIgGAsQZWz9ShFvk", parse_mode=None)
key = "247319"


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "^Привет. Это личный дневник Mark3715.^")
    bot.send_message(message.chat.id, "^Введите пароль для авторизации.^")


@bot.message_handler(content_types='text')
def handle_message(message):
    if message.text == key:
        bot.send_message(message.chat.id, "^Открыт доступ к странице дневника #356^")
        bot.send_message(message.chat.id, "^Сегодня наконец-то всё готово. Я заминировал этот чёртов университет и "
                                          "скоро он взлетит на воздух. Я расположил три датчика в обычных коробках. "
                                          "Все они реагируют на прикосновение человека. Две поменьше выйдут из строя "
                                          "только если покинут зону действия в 1м. А третью, самую большую, "
                                          "нужно разрушить в хлам! И самое главное, даже если останется хоть одна "
                                          "рабочая коробка, всё равно план сработает. Я оставил на коробках второй "
                                          "пароль для входа в аккаунт и если ты это читаешь, то спасибо, "
                                          "ты активировал таймер. Программа взрыва уже запущена. Судя по всему у тебя "
                                          "осталось около 5 минут чтобы всё деактивировать. Правила есть, игрок есть, "
                                          "пусть начнётся ИГРА!^")
    else:
        bot.send_message(message.chat.id, "^ERROR_НЕПРАВИЛЬНЫЙ ПАРОЛЬ^")


bot.polling(none_stop=True)
