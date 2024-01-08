import sys
import re

pattern = r'[;\s,.]'
target = input().lower()
target_count = count = 0

for line in sys.stdin.readlines():
    if line == "EOF":
        break

    data = list(filter(lambda x: len(x) > 0, re.split(pattern, line.lower())))
    target_count += data.count(target)
    count += len(data)

print(f'{target_count},{count}')
