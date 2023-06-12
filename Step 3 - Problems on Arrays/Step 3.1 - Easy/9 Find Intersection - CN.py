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
def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    i = 0
    j = 0
    inter = []
    while i < n and j < m:
        if arr[i] < brr[j]:
            i += 1
        elif arr[i] > brr[j]:
            j += 1
        else:
            inter.append(arr[i])
            i += 1
            j += 1
    return inter


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        res = findArrayIntersection(arr, n, brr, m)
        for i in res:
            print(i, end=" ")
        print()
