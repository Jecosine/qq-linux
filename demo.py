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


import termios
from qqbot import _bot as bot,qqbotslot
import sys
import termios,fcntl,struct

class chat_window:
    def init(self,title):
        self.disable_io()
        self.title = title
        self.panel = []
        self.height ,self.width = self.get_size()
        self.cursor = 0
        
    def render_once(self):
        sys.stdout.write('\x1b[1;1H\x1b[0m')
        rows = self.height - 6
        if len(self.panel)<>0:
            for i in self.panel:
                if len(i[0]) > (self.width/2-1):
                    for j in range(len(i[0])//(self.width/2-1)+1):
                        if j<(len(i[0])//(self.width/2-1)):
                            sys.stdout.write('\x1b['+str(rows+j)+';1H\x1b[7m'+i[0][j*(self.width/2-1):(j+1)*(self.width/2-1)])
                        else:
                            sys.stdout.write('\x1b['+str(rows+j)+';1H\x1b[7m'+i[0][j*(self.width/2-1):])
                        rows += 1


    
    
    
    def flush_edit(self):
        sys.stdout.write('\x1b['+str(self.height-6)+';0H')
        sys.stdout.write('\x1b[J')
    
    def flush_screen(self):
        sys.stdout.write('\x1b['+str(height-1)+';'+str(self.width)+'H\x1b[0m'))
        sys.stdout.write('\x1b[2J\x1b[0m')
        
    def get_size(self):
        fd = sys.stdin.fileno()
        return struct.unpack('hh',fcntl.ioctl(fd,termios.TIOCGWINSZ,'xxxx'))

    def disable_io(self):
        termIn_new = termios.tcgetattr(0)
        termOut_new = termios.tcgetattr(1)
        self.termIn_old = termios.tcgetattr(0)
        self.termOut_old = termios.tcgetattr(1)
        #set termios.VTIME termios.VTMIN termios.ECHO and termios.ICANON
        termIn_new[3] &= ~(termios.ECHO | termios.ICANON)
        termOut_new[3] &= ~(termios.ECHO | termios.ICANON)
        termIn_new[6][termios.VTIME] = 1
        termOut_new[6][temrios.VTIME] = 1
        
        termIn_new[6][termios.VMIN] = 0
        termOut_new[6][termios.VMIN] = 0

        termios.tcsetattr(0,termios.TCSNOW,termIn_new)
        termios.tcsetattr(1,termios.TCSNOW,termOut_new)

    def recover_io(self):
        termios.tcsetattr(0,termios,TCSANOW,self.termIn_old)
        termios.tcsetattr(1,termios,TCSANOW,self.termOut_old)

    def
