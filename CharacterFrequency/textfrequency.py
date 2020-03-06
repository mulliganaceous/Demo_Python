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
        print("Permission Deined for {}".format(filename))
        filename = input("Enter a file name: ")


print("Byte analysis of file {}".format(filename))
bintxt = file.read()
byte_freq = []
for byte in range(0,FF + 1):
    byte_freq.append(0)

for b in bintxt:
    byte_freq[b] += 1

for byte in range(0,FF + 1):
    print("%02X:\t%7d\t%s" %(byte, byte_freq[byte], ascii(byte))) 
    
print("Total bytes: {}", len(bintxt))
