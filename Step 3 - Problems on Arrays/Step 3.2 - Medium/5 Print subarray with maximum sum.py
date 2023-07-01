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
def maxSubArray(arr):
    sum = 0
    mx = arr[0]
    start = 0
    end = 0
    for i, x in enumerate(arr):
        if sum == 0:
            start = i

        sum += x

        if sum > mx:
            end = i

        if sum < 0:
            sum = 0
    return arr[start : end + 1]


if __name__ == "__main__":
    for _ in range(int(input())):
        arr = list(map(int, input().strip().split()))
        print(maxSubArray(arr))
