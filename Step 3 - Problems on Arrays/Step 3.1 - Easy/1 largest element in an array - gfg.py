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

# User function Template for python3


def largest(arr, n):
    l = arr[0]
    for i in arr:
        l = max(i, l)
    return l


# {
# Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())

    while T > 0:
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(largest(a, n))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
