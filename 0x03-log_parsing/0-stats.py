@@ -1,41 +1,39 @@
#!/usr/bin/python3
"""Log Parsing
Write a script that reads stdin line by line and computes metrics:
"""
import sys

Log parsing
"""

total_file_size = 0
status = ['200', '301', '400', '401', '403', '404', '405', '500']
obj = dict.fromkeys(status, 0)
import sys

if __name__ == '__main__':

def printLogStat():
    """Print log statistics"""
    print("File size: {}".format(total_file_size))
    for key, value in sorted(obj.items()):
        if value > 0:
            print("{}: {}".format(key, value))
    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(filesize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

if __name__ == "__main__":
    count = 0
    try:
        for line in sys.stdin:
            line = line.split()
            count += 1
            data = line.split()
            try:
                total_file_size += int(line[-1])

                if line[-2] in status:
                    obj[line[-2]] += 1

            except (IndexError, ValueError):
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass

            if count % 10 == 0:
                printLogStat()
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        pass
    finally:
        printLogStat()
        print_stats(stats, filesize)
        raise
