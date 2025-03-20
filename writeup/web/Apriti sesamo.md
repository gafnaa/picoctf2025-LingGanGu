# Apriti sesamo

## Description

I found a web app that claims to be impossible to hack!
Try it [here](http://verbal-sleep.picoctf.net:56613/)!

## Solution

Try login with common username/password. 
http://verbal-sleep.picoctf.net:56613/impossibleLogin.php

But we can’t log in! So let’s use some hints from developers and see that we need to find backups files on emacs, for which we usually need to add `.old, .backup,. ~`.

Then, find this code:
```php
<?php
 if(isset($_POST[base64_decode("\144\130\x4e\154\x63\155\x35\x68\142\127\125\x3d")])&& isset($_POST[base64_decode("\143\x48\x64\x6b")]))
 {$yuf85e0677=$_POST[base64_decode("\144\x58\x4e\154\x63\x6d\65\150\x62\127\x55\75")];$rs35c246d5=$_POST[base64_decode("\143\x48\144\153")];
 if($yuf85e0677==$rs35c246d5){echo base64_decode("\x50\x47\112\x79\x4c\172\x35\x47\x59\127\154\163\132\127\x51\x68\111\x45\x35\166\x49\x47\132\163\131\127\x63\x67\x5a\155\71\171\111\x48\x6c\166\x64\x51\x3d\x3d");}else{if(sha1($yuf85e0677)===sha1($rs35c246d5)){
    echo file_get_contents(base64_decode("\x4c\151\64\166\x5a\x6d\x78\x68\x5a\x79\65\60\145\110\x51\75"));}else{echo base64_decode("\x50\107\112\171\x4c\x7a\65\107\x59\x57\154\x73\x5a\127\x51\x68\x49\105\x35\x76\111\x47\132\x73\131\127\x63\x67\x5a\155\71\x79\x49\110\154\x76\x64\x51\x3d\75");}}}?>
 ```

 Let's try to make it easier to understand.
```php
<?php
if(isset($_POST[“username”]) && isset($_POST[“password”])) {
$yuf85e0677 = $_POST[“username”];
$rs35c246d5 = $_POST[“password”];

if($yuf85e0677 == $rs35c246d5) {
echo “Success”;
} else {
if(sha1($yuf85e0677) === sha1($rs35c246d5)) {
echo file_get_contents(“../flag.txt”);
} else {
echo “Success”;
}
}
}
?>
```
It first decodes the parameter names using base64_decode

`base64_decode(“\144\130\x4e\154\x63\155\x35\x68\142\127\125\x3d”)` gives username
`base64_decode(“\143\x48\x64\x6b”)` gives password

Then it checks if both parameters exist in `$_POST`

When sending data this way

The variables
```php
$yuf85e0677 = $_POST[‘username’]
$rs35c246d5 = $_POST[‘pwd’]
```
Will store arrays instead of strings

Calling the sha1 function with an array in PHP triggers a warning and returns null
This means both calls
```php
sha1($yuf85e0677)
sha1($rs35c246d5)
```
Will return null making the condition
```php
if(sha1($yuf85e0677) === sha1($rs35c246d5))
```
Evaluate as `null === null` which is true

By submitting data as arrays we’re bypassing the SHA1 collision check without generating a hash collision.


use burpsuite to edit request

![apritiburp](/assets/apritiburp_zqit72ivx.PNG)
```
username[]=asa&pwd[]=as
```
then you will get the error message with the flag.
![apriti](/assets/apriti_2t9za39fb.PNG)

## Flag
    picoCTF{w3Ll_d3sErV3d_Ch4mp_b88bdb32}