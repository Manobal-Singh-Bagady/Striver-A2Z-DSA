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
    def is_palindrome(self, n):
        def reverseNum(n):
            ans = 0
            while n > 0:
                ans = ans * 10 + (n % 10)
                n //= 10
            return ans

        if n == reverseNum(n):
            return "Yes"
        else:
            return "No"


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.is_palindrome(n)
        print(ans)
# } Driver Code Ends
