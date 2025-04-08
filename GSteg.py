'''
Name: Joseph DiMartino
Program: 8 - GSteg
Description - Find the needle in the haystack (find hidden data within data)
'''
from datetime import datetime
import os

haystack_filename = "B2097152-duke.mp3.bmp"
offset = 0  # list offset position
DLEN = ""
FNAME = ""
HSIG = bytearray(b'STEG')  # set HSIG
#HSIG = bytearray()
#for char in "STEG":  # uncomment if looking for a different header than "STEG"
#    HSIG += bytes([ord(char)])
len_header = len(HSIG)

with open(haystack_filename, "rb") as rf:
    haystack = bytearray(rf.read())
    len_haystack = len(haystack)

    for i in range(0, len_haystack - len_header):
        if haystack[i:i + len_header] == HSIG:
            print(HSIG.decode('utf-8'))
            offset = i
            i += len_header  # shift I to after "STEG"

            for j in range(i, len_haystack): # find file name (FNAME)
                if haystack[j:j+1] == bytearray(b'\x00'):
                    i = j+1
                    break
                FNAME += chr(haystack[j])
            print(FNAME)

            for j in range(i, len_haystack):
                if haystack[j:j+3].decode('utf-8') == "L8R":
                    break
            DLEN = int.from_bytes(haystack[i:j], byteorder='big')
            i = j
            print(DLEN)
            data = haystack[i:i+DLEN]
            break
            # exited for loop since we have all the data we need

    t = datetime.now().strftime("%Y%m%d-%H%M%S")  # get current time stamp
    FNAME = f"{t}-{FNAME}"  # name a file and write to it

    output_path = os.path.expanduser(f"~/Desktop/CSC330Files/outputs/{FNAME}")
    with open(f"{output_path}", "wb") as wf:
        wf.write(data)
