from demo import Chat_Window
from qqbot import _bot as bot,qqbotslot

if __name__ == "__main__":
    bot.Login()
    chat = Chat_Window('test')
    @qqbotslot
    def onQQMessage(bot,contact,member,content):
        chat.add_message(contact,member,content)
        chat.refresh_message()

