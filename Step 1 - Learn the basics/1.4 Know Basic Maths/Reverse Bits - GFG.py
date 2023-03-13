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
    def reversedBits(self, X):
        # code here
        s = bin(X)[2:]
        S = "0"*(32-len(s))+s
        return int(''.join(list(reversed(S))),2)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        X = int(input())

        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends
