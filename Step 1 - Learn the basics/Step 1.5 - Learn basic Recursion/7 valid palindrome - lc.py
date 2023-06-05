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

# ***** NOT WORKING *****
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         s = "".join(c.lower() for c in S if c.isalnum())
#         st = 0
#         ed = len(s) - 1
#         if st >= ed:
#             return 1
#         if s[st] != s[ed]:
#             return 0
#         return self.isPalindrome(s[1 : len(s) - 1])


# sys.setrecursionlimit(10**6)


class Solution(object):
    def isPalindrome(self, S):
        """
        :type s: str
        :rtype: bool
        """
        s = [c.lower() for c in S if c.isalnum()]

        if len(s) == 0 or len(s) == 1:
            return True
        else:
            for i in range(len(s) // 2):
                if s[i] != s[-i - 1]:
                    return False
            return True


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        print(ob.isPalindrome(S))
