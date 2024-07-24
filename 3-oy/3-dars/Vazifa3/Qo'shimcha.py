import telebot


class TelegramSms:
    def __init__(self, username, tg_id):
        self.username = username
        self.tg_id = tg_id
        self.bot = telebot.TeleBot('SAMANDARS_BOT')

    def send(self, message):
        self.bot.send_message(self.tg_id, message)


if __name__ == "__main__":
    bot_token = 'SAMANDARS_BOT'
    user1 = TelegramSms("user1", "123456789")
    user1.send("Hello from your Telegram bot!")
