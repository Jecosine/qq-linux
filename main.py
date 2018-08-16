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
        self.exit = False

    def main_session(self):
        #Init screen
        bi.close_iodisplay()
        sys.stdout.write('\x1b[3J\x1b[0m')
        while not self.exit:

            sys.stdout.write('\x1b[30;1H\x1b[7m'+' '*30+'\x1b[0m')
            
            sys.stdout.write('\x1b[31;1H\x1b[J')
            sys.stdout.write('\x1b[36;1H\x1b[46m\x1b[30m'+'a'*30+'\x1b[0m\x1b[31;1H')
            s = ''
            #bi.restore()
            c = sys.stdin.read(1)
            lastchar = ''
            m = ''
            while (c):
                s = ''
                if ord(c) not in range(128):
                    s = c
                    s += sys.stdin.read(2)
                    sys.stdout.write(s)
                    sys.stdout.flush()
                    lastchar = s[-1]
                    m += s
                elif c == "\n":
                    break
                elif c=="/":
                    sys.stdout.write('\x1b[36;1H')
                    command = sys.stdin.readline()
                    sys.stdout.write(command)
                    if "q" in command:
                        bi.restore()
                        sys.exit()
                else:
                    lastchar = c
                    m += c
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    lastchar = c
                c = sys.stdin.read(1)
             #   time.sleep(0.1)
            row = calculate(content)
            if (m):
                # content.append(['User MJ',m])
                if row > 28:   
                    sys.stdout.write('\x1b['+str(29)+';1H\x1b[7m'+content[-1][0]+'\n\x1b[0m\x1b[K'+content[-1][1]+'\x1b[K\x1b[0m\n'+'\x1b[K\x1b[0m\n'*7)
                else:

                    sys.stdout.write('\x1b['+str(row)+';1H\x1b[7m'+content[-1][0]+'\n\x1b[0m'+content[-1][1])   

            time.sleep(0.1)
                
        #Poll message every 1s
        #Show polled message
        


        
