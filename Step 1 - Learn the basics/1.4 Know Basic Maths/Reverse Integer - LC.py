# ---------------- MSB's Coding Template ---------------- #
'''
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
'''

# ---I/O from file---#
import sys
try:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    sys.stderr = open("error.txt", "w")
except:
    pass


# ---------------------- Code Starts Here ----------------------#


# User function Template for python3

class Solution:
    def reversedBits(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1

        x *= sign

        ans = 0
        i = len(str(x))-1
        while x > 0:
            ans += x % 10 * 10**i
            x //= 10
            i -= 1

        if ans*sign < -2**31 or ans*sign > (2**31-1):
            return 0
        else:
            return ans*sign


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x = int(input())

        ob = Solution()
        print(ob.reversedBits(x))
# } Driver Code Ends
