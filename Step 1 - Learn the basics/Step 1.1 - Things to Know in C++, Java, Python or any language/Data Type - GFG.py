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

# link - https://practice.geeksforgeeks.org/problems/data-type-1666706751/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=data-type

# ---------------------- Code Starts Here ----------------------#

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3


class Solution:
    def dataTypeSize(self, str):
        if str == "Character":
            return 1
        elif str == "Integer":
            return 4
        elif str == "Long":
            return 8
        elif str == "Float":
            return 4
        else:
            return 8


# {
# Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str = input()
        ob = Solution()
        res = ob.dataTypeSize(str)
        print(res)
# } Driver Code Ends
