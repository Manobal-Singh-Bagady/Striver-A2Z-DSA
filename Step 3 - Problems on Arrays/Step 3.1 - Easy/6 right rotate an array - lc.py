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


class Solution:
    def rotate(self, arr: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        k %= n
        arr[: n - k] = reversed(arr[: n - k])
        arr[n - k :] = reversed(arr[n - k :])
        arr.reverse()


if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n, k = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ob.rotate(arr, k)
        for i in range(n):
            print(arr[i], end=" ")
        print()
        tc -= 1
