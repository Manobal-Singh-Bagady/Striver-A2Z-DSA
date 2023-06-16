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


class Solution:
    def sort012(self, arr, n):
        lo = 0
        mid = 0
        high = n - 1
        while mid <= high:
            if arr[mid] == 0:
                arr[lo], arr[mid] = arr[mid], arr[lo]
                lo += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[high], arr[mid] = arr[mid], arr[high]
                high -= 1
        # for i in range(n):
        #     if arr[mid] == 0:
        #         arr[lo], arr[mid] = arr[mid], arr[lo]
        #         lo += 1
        #         mid += 1
        #     elif arr[mid] == 1:
        #         mid += 1
        #     elif arr[mid] == 2:
        #         if high < mid:
        #             break
        #         arr[high], arr[mid] = arr[mid], arr[high]
        #         high -= 1
        # Python specific answer.
        """
        ones = 0
        zeros = 0
        twos = 0
        for i in arr:
            if i == 0:
                zeros += 1
            elif i == 1:
                ones += 1
            else:
                twos += 1

        arr[:] = [0]*zeros + [1]*ones + [2]*twos
        """


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sort012(arr, n)
        for i in arr:
            print(i, end=" ")
        print()

# } Driver Code Ends
