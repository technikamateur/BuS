page_size = int(input("Seitengröße in KiB: "))
text = int(input("Text in KiB: "))
data = int(input("Data in KiB: "))
bss = int(input("BSS in KiB: "))
stack = int(input("Stack in KiB: "))

start = page_size*1024


if text % page_size == 0:
    end = start+text*1024-1
else:
    end = start+((text // page_size)*page_size + page_size)*1024-1
textl = ["Text", hex(start), hex(end), "ro, ex, u", "", "binary", "0x00??"]
start = end + 1


if data % page_size == 0:
    end = start+data*1024-1
else:
    end = start+((data // page_size)*page_size + page_size)*1024-1
datal = ["Data", hex(start), hex(end), "rw, u", "", "binary", "0x5???"]
start = end + 1


if bss % page_size == 0:
    end = start+bss*1024-1
else:
    end = start+((bss // page_size)*page_size + page_size)*1024-1
bssl = ["BSS", hex(start), hex(end), "rw, u", "zero init", "", ""]
start = end + 1

end = int("bfffffff", 16)
if stack % page_size == 0:
    start = end-stack*1024+1
else:
    start = end-((stack // page_size)*page_size + page_size)*1024+1
stackl = ["Stack", hex(start), hex(end), "rw, u", "GD", "", ""]

print("\n")
print("Hier ist die Region Map. Keine Granatie - Viel Spaß :)")
print("\n")
print("| ".join([str(l).rjust(3) for l in ["Name", "Start", "Ende", "Rechte", "Options", "Inode", "Offset"]]))
print("-------------------------------------------------\n")
print("| ".join([str(l).rjust(3) for l in textl]))
print("| ".join([str(l).rjust(3) for l in datal]))
print("| ".join([str(l).rjust(3) for l in bssl]))
print("| ".join([str(l).rjust(3) for l in stackl]))
print("| ".join([str(l).rjust(3) for l in ["OS", "0xC0000000 (7x0)", "0xFFFFFFFF (7xF)", "rw, ex, s"]]))
