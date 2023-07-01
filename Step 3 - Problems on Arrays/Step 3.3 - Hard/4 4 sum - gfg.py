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


# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        ans = []
        arr.sort()
        n = len(arr)
        for i in range(n):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    sum = arr[i] + arr[j] + arr[k] + arr[l]
                    if sum < k:
                        k += 1
                    elif sum > k:
                        l -= 1
                    else:
                        ans.append([arr[i], arr[j], arr[k], arr[l]])
                        k += 1
                        l -= 1
                        while k < l and arr[k] == arr[k - 1]:
                            k += 1
                        while k < l and arr[l] == arr[l + 1]:
                            l -= 1
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3


# Main
if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        n, k = map(int, input().split())
        # print(n, k)
        a = list(map(int, input().strip().split()))[:n]
        # print(a)
        ob = Solution()
        ans = ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if len(ans) == 0:
            print(-1, end="")
        print()


# } Driver Code Ends
