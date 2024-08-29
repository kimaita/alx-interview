#!/usr/bin/python3
"""Contains a class for handling a log stream"""

import re
import signal
import sys


class LogSession:
    """Defines a log session, keeping tally of log records"""

    codes = [200, 301, 400, 401, 403, 404, 405, 500]

    def __init__(self):
        self._file_size = 0
        self._status_codes = dict.fromkeys(self.codes, 0)

    def parse_line(self, line: str):
        """Parses a log line to extract and update the HTTP status code and
        size"""
        ptn = re.compile(
            r"(?P<ip>(\d{1,3}\.?){4}).*\[(?P<time>([\d:\.\- ])*)\] "
            r'"GET /projects/260 HTTP/1.1" (?P<code>\d{3}) (?P<size>\d{,4})$'
        )
        match = ptn.match(line)

        if match:
            self._file_size += int(match.group("size"))
            self._status_codes[int(match.group("code"))] += 1

    def print_stats(self):
        """Prints the total fize size for the procssed logs and occurences
        of each HTTP code
        """
        print("File size: {}".format(self._file_size))
        for code, count in self._status_codes.items():
            if count:
                print("{}: {}".format(code, count))

    def signal_handler(self, signum, frame):
        """Handles an intercepted a Ctrl+C signal"""
        # print("Signal handler called with signal", signum)
        self.print_stats()


if __name__ == "__main__":
    logs = LogSession()
    signal.signal(signal.SIGINT, logs.signal_handler)
    lines = 0

    for log in sys.stdin:
        logs.parse_line(log)
        lines += 1

        if not lines % 10:
            logs.print_stats()
