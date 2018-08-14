from demo import Chat_Window
from qqbot import _bot as bot,qqbotslot

if __name__ == "__main__":
    bot.Login()
    chat = Chat_Window('test')
    #set chat manually
    @qqbotslot
    def onQQMessage(bot,contact,member,content):
        if contact.name == "test":
            chat.add_message(contact,member,content)
            chat.refresh_message()

