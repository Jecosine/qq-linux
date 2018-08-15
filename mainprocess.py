#from demo import Chat_Window
from qqbot import _bot as bot,qqbotslot,RunBot

if __name__ == "__main__":
    bot.Login(['-q','1598225432'])
    #chat = Chat_Window('test')
    #set chat manually
    @qqbotslot
    def onQQMessage(bot,contact,member,content):
        if contact.name == "test":
            echo_1()
            #chat.add_message(contact,member,content)
            #chat.refresh_message()
    def echo_1():
        print "\x1b[1;1H\x1b[2J\x1b[7m"+member.card+"\n\x1b[0m"+content+"\n", 
    
    RunBot()
