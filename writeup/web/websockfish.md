# Websockfish

## Description
Can you win in a convincing manner against this chess bot? He won't go easy on you!
You can find the challenge here.
## Solution

the vulnerability turned out to be surprisingly simple. The challenge description asked us to “win in a convincing manner,” which suggested we needed to make the chess engine believe it’s in a completely lost position.

```js
if (event.data.includes("mate")) {
            message = "mate " + parseInt(splitString[9]);
          } else {
            message = "eval " + parseInt(splitString[9]);
          }
          sendMessage(message);
```

by opening the browser console and sending an extremely negative evaluation score:

```jsx
sendMessage("eval -99999");
```

```

Huh???? How can I be losing this badly... I resign... here's your flag: picoCTF{c1i3nt_s1d3_w3b_s0ck3t5_9b154ed7}
```

## Flag
    picoCTF{c1i3nt_s1d3_w3b_s0ck3t5_9b154ed7}