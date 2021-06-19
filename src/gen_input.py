import struct
CMP = 0x10000
HLT = 0x08000
J   = 0x04000
CO  = 0x02000
CE  = 0x01000
MI  = 0x00800
MO  = 0x00400
AI  = 0x00200
AO  = 0x00100
BI  = 0x00080
OI  = 0x00040
SUB = 0x00020
ADD = 0x00010
II  = 0x00008
IO  = 0x00004
CR  = 0x00002

# ADD 20,55  20+55=75
# MOV B,A   A->B
# OTA    A->OUTPUT
# CMP B,A   B==A?
# OTA        OUTPUT B==A
# MOV A,99   A <- 99
# SUB B,A     A-B=24
# OTA         A->OUTPUT
# HLT        STOP


ops = [
    [CO|MI, MO|II|CE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, CR],#0x00 NOP
    [CO|MI, MO|II|CE, IO|MI, MO|AI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x01 MOV A
    [CO|MI, MO|II|CE, ADD|AI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0],#0x02 ADD A+B
    [CO|MI, MO|II|CE, SUB|AI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0],#0x03 SUB A-B
    [CO|MI, MO|II|CE, AO|BI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x04 MOV B,A
    [CO|MI, MO|II|CE, CMP|AI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0],#0x05 CMP A,B
    [CO|MI, MO|II|CE, IO|MI, MO|BI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x06  MOV B
    [CO|MI, MO|II|CE, HLT, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x07
    [CO|MI, MO|II|CE, HLT, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x08
    [CO|MI, MO|II|CE, HLT, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x09
    [CO|MI, MO|II|CE, HLT, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x0A
    [CO|MI, MO|II|CE, IO|J, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x0B Jump*
    [CO|MI, MO|II|CE, IO|MI, MO|OI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x0C OTM* (output Memory)
    [CO|MI, MO|II|CE, OI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x0D OTB (output Bus)
    [CO|MI, MO|II|CE, AO|OI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x0E OTA(output A)
    [HLT, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #0x0F HLT
]

class Command:
    def __init__(self):
        self.cmd = ''
        self.index = 0
        self.num_list = []
        self.out = open("../data/input","w+")
        self.out.write("v2.0 raw\n")
    def add_cmd(self,cmd_num,data = None):
        self.index += 1
        if data != None:
            self.cmd += "%1xI "%(cmd_num)
            self.num_list.append(data)
        else:
            self.cmd += "%1x0 "%(cmd_num)
    def out_cmd(self):
        for each_num in self.num_list:
            self.cmd = self.cmd.replace("I", "%1x"%self.index, 1)
            self.cmd += "%02x "%(each_num)
            # print("%02x "%(each_num),each_num,self.cmd)
            self.index += 1
        # print(self.cmd)
        self.out.write(self.cmd)

f = open("./input.txt","r+")
my_cmd = Command()
for i in f:
    i = i.strip()
    if i[:3] == 'MOV':
        temp = i.split(' ')[1]
        num1,num2 = temp.split(',')
        if num1 == 'B' and num2 == 'A':
            my_cmd.add_cmd(4)
        elif num1 == 'B':
            my_cmd.add_cmd(6,int(num2))
        elif num1 == 'A':
            my_cmd.add_cmd(1,int(num2))
    elif i[:3] == 'ADD':
        temp = i.split(' ')[1]
        num1,num2 = temp.split(',')
        if num1 == 'B' and num2 == 'A':
            my_cmd.add_cmd(2)
        elif num1 == 'A':
            my_cmd.add_cmd(6,int(num2))
            my_cmd.add_cmd(2)
        else:
            my_cmd.add_cmd(1,int(num1))
            my_cmd.add_cmd(6,int(num2))
            my_cmd.add_cmd(2)

    elif i[:3] == 'SUB':
        temp = i.split(' ')[1]
        num1,num2 = temp.split(',')
        if num1 == 'B' and num2 == 'A':
            my_cmd.add_cmd(3)
        elif num1 == 'A':
            my_cmd.add_cmd(6,int(num2))
            my_cmd.add_cmd(3)
        else:
            my_cmd.add_cmd(1,int(num1))
            my_cmd.add_cmd(6,int(num2))
            my_cmd.add_cmd(3)
    elif i[:3] == 'CMP':
        temp = i.split(' ')[1]
        num1,num2 = temp.split(',')
        if num1 == 'B' and num2 == 'A':
            my_cmd.add_cmd(5)
        elif num1 == 'A':
            my_cmd.add_cmd(6,int(num2))
            my_cmd.add_cmd(5)
        elif num1 == 'B':
            my_cmd.add_cmd(1,int(num2))
            my_cmd.add_cmd(5)
        else:
            my_cmd.add_cmd(1,int(num1))
            my_cmd.add_cmd(6,int(num2))
            my_cmd.add_cmd(5)

    elif i[:3] == 'OTA':
        my_cmd.add_cmd(14)
    elif i[:3] == 'HLT':
        my_cmd.add_cmd(15)
    elif i[:3] == 'NOP':
        my_cmd.add_cmd(0)

my_cmd.out_cmd()