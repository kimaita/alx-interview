# Log Parsing

The objective here is to parse and process a data stream in real-time. We will be reading a stream of logs fron `stdin` and parsing them to keep a count of HTTP code occurrences and the cumulative file size.

## Specifications

Input format:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

Possible status codes:

```
200 301 400 401 403 404 405 500
```

After every 10 lines and/or a keyboard interruption (`CTRL + C`), we print the total file size and the status code occurences.

## Example

```bash
$ ./0-gen.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./0-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
```
