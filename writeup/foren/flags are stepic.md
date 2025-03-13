# flags are stepic
by Rey

## First things:
- The author provided a website that has many pictures of country flags.
- The author gave a hint that says "country that doesn't exist may have the flag"
- The title is "flags are stepic"

With those known hints, we can get the flag by these steps

## Steps
1. Open the website
2. Find the flag that is not an any country flag. I've found there is one flag says "uplink network" that is very obviously that it is not a country flag.
3. I downloaded the flag
4. Because the problem titled "stepic" so I assume that the flag is encrypted inside the picture with stepic.
5. So I created code to decrypt the file with python using stepic.

The code:
```
import stepic
from PIL import Image

def decode_message(image_path):
    img = Image.open(image_path)
    decoded_message = stepic.decode(img)
    return decoded_message.decode('utf-8')

image_path = "hidden_message.png"
message = decode_message(image_path)
print("Decoded message:", message)
```

6. Finally we got the flag


The flag is:
picoCTF{fl4g_h45_fl4g51d83cb1}
