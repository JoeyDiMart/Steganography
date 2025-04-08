'''
Name: Joseph DiMartino
Program: 8 - GSteg
Description - Find the needle in the haystack (find hidden data within data)
'''

haystack_filename = "B2097152-duke.mp3.bmp"
offsets = []  # list of offsets incase data is spread out
#header = bytearray()
#for char in "STEG":  # uncomment if looking for a different header than "STEG"
#    header += bytes([ord(char)])

header = bytearray(b'STEG')
len_header = len(header)

with open(haystack_filename, "rb") as f:
    haystack = bytearray(f.read())
    len_haystack = len(haystack)

    for i in range(0, len_haystack - len_header):
        if haystack[i:i + len_header] == header:
            offsets.append(i)
            print(haystack[i:i+len(header)+30])
            i += len_header  # shift I to after "STEG"
            print(haystack[i])
            print(haystack[i:i+10])
