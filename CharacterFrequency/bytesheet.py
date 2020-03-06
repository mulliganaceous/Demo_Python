FF = 255

filename = input("Enter a file name: ")
file = None

while not file:
    try:
        file = open(filename, "rb")
    except (FileNotFoundError):
        print("File Name not found!")
        filename = input("Enter a file name: ")
    except (PermissionError):
        print("Permission Denied for {}".format(filename))
        filename = input("Enter a file name: ")

outputname = open("bytesheet.txt", "w")
outputname.write("Byte analysis of file {}\n".format(filename))
bintxt = file.read()
file.close()

byte_freq = []
count = 0
for b in bintxt:
    outputname.write(str("%02X" %b))
    if count % 16 < 15:
        outputname.write(" ")
    else:
        outputname.write("\n")
    count += 1
    
print("Total bytes: {}", len(bintxt))
outputname.close()
