# hashcrack

## Description

A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?
Access the server using nc verbal-sleep.picoctf.net 57192

## Solution

access the server

```sh
$ nc verbal-sleep.picoctf.net 57192
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash:
```
The hash `482c811da5d5b4bc6d497ffa98491e38` is an MD5 hash. Let's try to decrypt it.
The decryption result shows that this hash is a representation of the string: "password123"

```
Flag is yet to be revealed!! Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Enter the password for the identified hash:  
```

The hash `b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3` is a SHA-1 hash. Let's try to decrypt it.
The decryption result shows that the original string of this hash is: "letmein"

```
Almost there!! Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
Enter the password for the identified hash:
```

​The hash 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745 is a SHA-256 hash. After doing some searching, I found that this hash corresponds to the string:​ "qwerty098"

```
Correct! You've cracked the SHA-256 hash with a secret found.
The flag is: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_29028be8}
```

## Flag
    picoCTF{UseStr0nG_h@shEs_&PaSswDs!_29028be8}
