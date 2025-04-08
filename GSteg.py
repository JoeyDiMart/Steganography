'''
Name: Joseph DiMartino
Program: 8 - GSteg
Description - Find the needle in the haystack (find hidden data within data)
'''

haystack_filename = "B2097152-duke.mp3.bmp"
offsets = []  # list of offsets incase data is spread out
#HSIG = bytearray()
#for char in "STEG":  # uncomment if looking for a different header than "STEG"
#    HSIG += bytes([ord(char)])

HSIG = bytearray(b'STEG')
len_header = len(HSIG)

with open(haystack_filename, "rb") as f:
    haystack = bytearray(f.read())
    len_haystack = len(haystack)

    for i in range(0, len_haystack - len_header):
        if haystack[i:i + len_header] == HSIG:
            offsets.append(i)
            i += len_header  # shift I to after "STEG"
            FNAME = ""
            for j in range(i, len_haystack):
                if haystack[j:j+1] == bytearray(b'\x00'):
                    break
                FNAME += chr(haystack[j])
            print(FNAME)

