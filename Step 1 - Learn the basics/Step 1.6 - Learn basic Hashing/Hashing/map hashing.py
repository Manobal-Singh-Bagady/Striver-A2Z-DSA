# ---------------- MSB's Coding Template ---------------- #
"""
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
"""

# ---I/O from file---#
import sys

try:
    sys.stdin = open("input.txt", "r", encoding="UTF-8")
    sys.stdout = open("output.txt", "w", encoding="UTF-8")
    sys.stderr = open("output.txt", "w", encoding="UTF-8")
except FileNotFoundError as __:
    pass


# ---------------------- Code Starts Here ----------------------#


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    hashmap = {}
    for i in arr:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    for _ in range(int(input())):
        x = int(input())
        if x in hashmap:
            print(hashmap[x])
        else:
            print(0)
