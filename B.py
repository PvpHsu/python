import sys
from collections import Counter

c = Counter(
    sys.stdin.read().strip().lower().split()
)

print(','.join(list(map(lambda x: str(x[1]), c.most_common(3)))))
