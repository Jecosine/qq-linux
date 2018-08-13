from qqbot import _bot as bot

class QQInstance():
    def __init__(self):
        try:
            bot.Login()
        except:
            print "Login Failed"
        else:
            self.bot = bot
            self.get_buddy_list()
            self.get_group_list()
            

    def get_buddy_list(self):
        self.buddy_list = self.bot.List('buddy')
    
    def get_group_list(self):
        self.group_list = self.bot.List('group')
    
    def send_message(contact,message):
        try:
            self.bot.SendTo()
        except:
            raise "Send Failed,check your network or restart this application"
        else:
            pass
            #show sended message on windows

    def 


    #Generate recent chat list and friends or group chats list
    def generate_lists(self):
        return 0    
    
    #Generate chat window after double click
    def popup_chat_window(self):
        #popup new window

    def initialize_main_window(self):
        #set layouts and fill informations

    #Trigger on new message comes
    def update_state(self):
        #update the information of each title
        #update the chatting windows information
