import struct

HLT = 0x8000
J   = 0x4000
CO  = 0x2000
CE  = 0x1000
MI  = 0x0800
MO  = 0x0400
AI  = 0x0200
AO  = 0x0100
BI  = 0x0080
OI  = 0x0040
SUB = 0x0020
ADD = 0x0010
II  = 0x0008
IO  = 0x0004
CR  = 0x0002
CMP = 0x0001

# ops = [
#     [CO|MI, MO|II|CE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, CR],#0x00 NOP
#     [CO|MI, MO|II|CE, IO|MI, MO|AI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x01 MOV A
#     [CO|MI, MO|II|CE, IO|MI, MO|BI, ADD|AI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x02 ADD num1,num2
#     [CO|MI, MO|II|CE, IO|MI, MO|BI, SUB|AI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x03 SUB *
#     [CO|MI, MO|II|CE, AO|BI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x04 MOV B,A
#     [CO|MI, MO|II|CE, IO|MI, MO|BI, CMP|AI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x05 CMP *
#     [CO|MI, MO|II|CE, IO|MI, MO|BI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x06
#     [CO|MI, MO|II|CE, ADD|AI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x07 ADD A B
#     [CO|MI, MO|II|CE, HLT, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x08
#     [CO|MI, MO|II|CE, HLT, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x09
#     [CO|MI, MO|II|CE, HLT, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x0A
#     [CO|MI, MO|II|CE, IO|J, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x0B Jump*
#     [CO|MI, MO|II|CE, IO|MI, MO|OI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x0C OTM* (output Memory)
#     [CO|MI, MO|II|CE, OI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x0D OTB (output Bus)
#     [CO|MI, MO|II|CE, AO|OI, CR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0x0E OTA(output A)
#     [HLT, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #0x0F HLT
# ]

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

f = open("../data/code","w")
f.write("v2.0 raw\n")
# f.write(HLT)
for i in ops:
    # print(len(i))
    for j in i:
        
        f.write("%04x "%j)
f.close()
