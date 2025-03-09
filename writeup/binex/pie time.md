# Pie Time

## Description
Can you try to get the flag? Beware we have PIE!
Connect to the program with netcat:
$ nc rescued-float.picoctf.net 50219
The program's source code can be downloaded here. The binary can be downloaded here.

## Solution

Use ```disas win``` to get the offset of ```win()``` relative to the binary.
Use ```disas main``` to get the offset of ```main()```.

```sh
$ gdb
(gdb) file vuln
Reading symbols from vuln...
(No debugging symbols found in vuln)
(gdb) disas win
Dump of assembler code for function win:
   0x00000000000012a7 <+0>:     endbr64
   0x00000000000012ab <+4>:     push   %rbp
   0x00000000000012ac <+5>:     mov    %rsp,%rbp
   0x00000000000012af <+8>:     sub    $0x10,%rsp
   0x00000000000012b3 <+12>:    lea    0xd74(%rip),%rdi        # 0x202e
   0x00000000000012ba <+19>:    call   0x1100 <puts@plt>
   0x00000000000012bf <+24>:    lea    0xd71(%rip),%rsi        # 0x2037
   0x00000000000012c6 <+31>:    lea    0xd6c(%rip),%rdi        # 0x2039
   0x00000000000012cd <+38>:    call   0x1170 <fopen@plt>
   0x00000000000012d2 <+43>:    mov    %rax,-0x8(%rbp)
   0x00000000000012d6 <+47>:    cmpq   $0x0,-0x8(%rbp)
   0x00000000000012db <+52>:    jne    0x12f3 <win+76>
   0x00000000000012dd <+54>:    lea    0xd5e(%rip),%rdi        # 0x2042
   0x00000000000012e4 <+61>:    call   0x1100 <puts@plt>
   0x00000000000012e9 <+66>:    mov    $0x0,%edi
   0x00000000000012ee <+71>:    call   0x1190 <exit@plt>
   0x00000000000012f3 <+76>:    mov    -0x8(%rbp),%rax
   0x00000000000012f7 <+80>:    mov    %rax,%rdi
   0x00000000000012fa <+83>:    call   0x1140 <fgetc@plt>
   0x00000000000012ff <+88>:    mov    %al,-0x9(%rbp)
   0x0000000000001302 <+91>:    jmp    0x131e <win+119>
   0x0000000000001304 <+93>:    movsbl -0x9(%rbp),%eax
   0x0000000000001308 <+97>:    mov    %eax,%edi
   0x000000000000130a <+99>:    call   0x10f0 <putchar@plt>
   0x000000000000130f <+104>:   mov    -0x8(%rbp),%rax
   0x0000000000001313 <+108>:   mov    %rax,%rdi
   0x0000000000001316 <+111>:   call   0x1140 <fgetc@plt>
   0x000000000000131b <+116>:   mov    %al,-0x9(%rbp)
--Type <RET> for more, q to quit, c to continue without paging--q
Quit
(gdb) disas main
Dump of assembler code for function main:
   0x000000000000133d <+0>:     endbr64
   0x0000000000001341 <+4>:     push   %rbp
   0x0000000000001342 <+5>:     mov    %rsp,%rbp
   0x0000000000001345 <+8>:     sub    $0x20,%rsp
   0x0000000000001349 <+12>:    mov    %fs:0x28,%rax
   0x0000000000001352 <+21>:    mov    %rax,-0x8(%rbp)
   0x0000000000001356 <+25>:    xor    %eax,%eax
   0x0000000000001358 <+27>:    lea    -0xd6(%rip),%rsi        # 0x1289 <segfault_handler>
   0x000000000000135f <+34>:    mov    $0xb,%edi
   0x0000000000001364 <+39>:    call   0x1150 <signal@plt>
   0x0000000000001369 <+44>:    mov    0x2ca0(%rip),%rax        # 0x4010 <stdout@@GLIBC_2.2.5>
   0x0000000000001370 <+51>:    mov    $0x0,%ecx
   0x0000000000001375 <+56>:    mov    $0x2,%edx
   0x000000000000137a <+61>:    mov    $0x0,%esi
   0x000000000000137f <+66>:    mov    %rax,%rdi
   0x0000000000001382 <+69>:    call   0x1160 <setvbuf@plt>
   0x0000000000001387 <+74>:    lea    -0x51(%rip),%rsi        # 0x133d <main>
   0x000000000000138e <+81>:    lea    0xcbf(%rip),%rdi        # 0x2054
   0x0000000000001395 <+88>:    mov    $0x0,%eax
   0x000000000000139a <+93>:    call   0x1130 <printf@plt>
   0x000000000000139f <+98>:    lea    0xcca(%rip),%rdi        # 0x2070
   0x00000000000013a6 <+105>:   mov    $0x0,%eax
   0x00000000000013ab <+110>:   call   0x1130 <printf@plt>
   0x00000000000013b0 <+115>:   lea    -0x18(%rbp),%rax
   0x00000000000013b4 <+119>:   mov    %rax,%rsi
   0x00000000000013b7 <+122>:   lea    0xce0(%rip),%rdi        # 0x209e
   0x00000000000013be <+129>:   mov    $0x0,%eax
   0x00000000000013c3 <+134>:   call   0x1180 <__isoc99_scanf@plt>
--Type <RET> for more, q to quit, c to continue without paging--Quit
(gdb) exit
```

Get the address of ```main()``` from the program output.
Calculate the address of ```win()``` by adding its relative offset to ```main()```.
Enter the address of ```win()``` when prompted by the program.


```sh
$ nc rescued-float.picoctf.net 61093
Address of main: 0x625f71ce333d
Enter the address to jump to, ex => 0x12345: 0x625f71ce32a7
Your input: 625f71ce32a7
You won!
picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_a267144a}
```
from the address of main() at runtime:
* Address of ```main()``` : ```0x625f71ce333d```
* Offset of ```win()``` from ```main()``` : ```0x12a7 - 0x133d = 0x96```

Address of win() that should be sent: 
```
win_addr = 0x625f71ce333d + (−0x96) = 0x625f71ce32a7
```

## Flag
    picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_a267144a}