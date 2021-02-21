from termcolor import colored

def split_bin(bi, offset, pt_two, pt_one):
    print("Offset: {}".format(hex(int(bi[-offset:], 2))))
    bi = bi[:-offset]
    print("2nd PT: {}".format(hex(int(bi[-pt_two:], 2))))
    bi = bi[:-pt_two]
    print("1st PT: {}\n".format(hex(int(bi, 2))))
    if len(bi) > pt_one:
        print("[Warning] The rest of your address is smaller than 1st PT bits. The result might be wrong.\n")

offset = int(input("Offset: "))
pt_two = int(input("2nd level PT: "))
pt_one = int(input("1st level PT: "))
architecture = input("Architecture e.g. 32: ")
if offset+pt_one+pt_two != int(architecture):
    print(colored("[Warning] Offset + pt_two + pt_one is not equal to your architecture. Only continue if you know, what you are doing!", "red"))
architecture = "0" + architecture + "b"
print("[INFO] You can exit with ctrl + c \n")

while True:
    address = int(input("Address: "), 16)
    address = format(address, architecture)

    print("\n[INFO] Your current architecture is: {}bit. ".format(len(address)))
    split_bin(address, offset, pt_two, pt_one)
