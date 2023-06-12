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
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b, n, m):
        """
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        """
        i = 0
        j = 0
        union = []
        union.append(min(a[i], b[j]))
        while i < n and j < m:
            if a[i] <= b[j]:
                if union[-1] != a[i]:
                    union.append(a[i])
                i += 1
            else:
                if union[-1] != b[j]:
                    union.append(b[j])
                j += 1
        while i < n:
            if a[i] != union[-1]:
                union.append(a[i])
            i += 1
        while j < m:
            if b[j] != union[-1]:
                union.append(b[j])
            j += 1
        return union


# {
# Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == "__main__":
    test_cases = int(input())
    for cases in range(test_cases):
        n, m = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b, n, m)
        for val in li:
            print(val, end=" ")
        print()
# } Driver Code Ends
