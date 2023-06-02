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


def reverseList(A, st, ed):
    if st >= ed:
        return
    A[st], A[ed] = A[ed], A[st]
    reverseList(A, st + 1, ed - 1)


if __name__ == "__main__":
    l = list(map(int, input().split()))
    reverseList(l, 0, len(l) - 1)
    print(l)
