import sys,time
import base_input as bi




#bi.close_iodisplay()

sys.stdout.write('\x1b[2J')

def get_input(i):
    c = sys.stdin.read(i)
    s = ''
    while(c):
        s = c
        c = sys.stdin.read(i)
    return s

while 1:
    sys.stdout.write('\x1b[30;1H\x1b[7m'+' '*30+'\x1b[0m')
    sys.stdout.write('\x1b[31;1H\x1b[J')
    s = ''
    bi.restore()
    c = sys.stdin.read(1)
    lastchar = ''
    m = ''
    while (lastchar <> '\n'):
        s = ''
        lastchar = ''
        if (c):
            if ord(c) not in range(128):
                s = c
                s += sys.stdin.read(2)
                sys.stdout.write(s)
                lastchar = s[-1]
                m += s
            else:
                lastchar = c
                m += c
                sys.stdout.write(c)
        c = sys.stdin.read(1)
        time.sleep(0.1)
    sys.stdout.write('\x1b[1;1H'+m)   
    time.sleep(0.1)
