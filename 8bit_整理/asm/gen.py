f1 = open("ge.asm","w+")
f2 = open("shi.asm","w+")
f3 = open("bai.asm","w+")
num_list = ["00111111","00000110","01011011","01001111","01100110","01101101","01111101","00000111","01111111","01101111"]

f1.write("ORG 0000H\n")
for i in range(256):
    f1.write("	DB "+num_list[int(i%10)]+"B\n")
            # fw1.write(hex[x/100] + " ");
            # fw2.write(hex[x/10%10] + " ");
f1.write("END")


f2.write("ORG 0000H\n")
for i in range(256):
    f2.write("	DB "+num_list[int(i/10%10)]+"B\n")
            # fw1.write(hex[x/100] + " ");
            # fw2.write(hex[x/10%10] + " ");
f2.write("END")

f3.write("ORG 0000H\n")
for i in range(256):
    f3.write("	DB "+num_list[int(i/100)]+"B\n")
            # fw1.write(hex[x/100] + " ");
            # fw2.write(hex[x/10%10] + " ");
f3.write("END")