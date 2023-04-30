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
    # Complete this function
    def printNos(self, N: int) -> int:
        if N == 0:
            return 1
        print(self.printNos(N - 1), end=" ")
        return N + 1


# {
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while T > 0:
        N = int(input())

        ob = Solution()

        ob.printNos(N)
        print()
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
