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


def reverseArray(arr, m):
    def reverse(arr, st, end):
        if st > end:
            return
        arr[st], arr[end] = arr[end], arr[st]
        reverse(arr, st + 1, end - 1)

    reverse(arr, m + 1, len(arr) - 1)
    return arr


if __name__ == "__main__":
    for _ in range(int(input())):
        arr = list(map(int, input().split()))
        print(reverseArray(arr, int(input())))
