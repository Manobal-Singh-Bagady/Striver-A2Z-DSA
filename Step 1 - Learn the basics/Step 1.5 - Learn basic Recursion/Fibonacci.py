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
    # Function to return list containing first n fibonacci numbers.
    def printFibb(self, N):
        if N == 1:
            return [1]
        if N == 2:
            return [1, 1]
        ans = self.printFibb(N - 1)
        ans.append(ans[-1] + ans[-2])
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == "__main__":
    t = int(input())
    for tcs in range(t):
        n = int(input())
        res = Solution().printFibb(n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
# } Driver Code Ends
