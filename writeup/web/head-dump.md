# head dump

## Description
Welcome to the challenge! In this challenge, you will explore a web application and find an endpoint that exposes a file containing a hidden flag.
The application is a simple blog website where you can read articles about various topics, including an article about API Documentation. Your goal is to explore the application and find the endpoint that generates files holding the server’s memory, where a secret flag is hidden.

## Solution

```sh
$ curl http://verbal-sleep.picoctf.net:60155/heapdump | grep "pico"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
 45 8704k   45 3979k    0     0   550k      0  0:00:15  0:00:07  0:00:08  807kpicoCTF{Pat!3nt_15_Th3_K3y_ad7ea5ae}
 90 8704k   90 7847k    0     0   768k      0  0:00:11  0:00:10  0:00:01 1254k"picoCTF News API",
"Welcome to the picoCTF News API documentation! This documentation provides a detailed overview of the available API endpoints for managing and retrieving news posts.",
"var options = {\n  \"swaggerDoc\": {\n    \"openapi\": \"3.0.0\",\n    \"info\": {\n      \"title\": \"picoCTF News API\",\n      \"version\": \"1.0.0\",\n      \"description\": \"Welcome to the picoCTF News API documentation! This documentation provides a detailed overview of the available API endpoints for managing and retrieving news posts.\"\n    },\n    \"paths\": {\n      \"/\": {\n        \"get\": {\n          \"tags\": [\n            \"Free\"\n          ],\n
 \"summary\": \"Welcome page\",\n          \"responses\": {\n            \"200\": {\n              \"description\": \"Returns a welcome message.\"\n            }\n          }\n        }\n      },\n      \"/about\": {\n        \"get\": {\n          \"tags\": [\n            \"Free\"\n          ],\n          \"summary\": \"About Us\",\n          \"responses\": {\n            \"200\": {\n              \"description\": \"Returns information about us.\"\n            }\n          }\n        }\n      },\n      \"/services\": {\n        \"get\": {\n          \"tags\": [\n            \"Free\"\n
 ],\n          \"summary\": \"Services\",\n          \"respon",
"verbal-sleep.picoctf.net:60155",
100 8704k  100 8704k    0     0   798k      0  0:00:10  0:00:10 --:--:-- 1287k
```

## Flag
    picoCTF{Pat!3nt_15_Th3_K3y_ad7ea5ae}
