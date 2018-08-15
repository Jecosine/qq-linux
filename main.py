from basic import BaseQSession as BaseSession
import base_input as bi
import sys

class Chat(BaseSession):
    def __init__(self):
        try:
            self.Login()
        except:
            self.Logger("Login Error")
        else:
            self.draft = "" #Save the draft when refreshing interrupt
            self.log = "" #Log displaying at bottom
            
    def main_session(self):
        #Init screen
        bi.close_iodisplay()
        sys.stdout.write('\x1b[3J\x1b[0m')
        #Poll message every 1s
        #Show polled message



        
