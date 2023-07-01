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
class Solution:
    count = 0
    # User function Template for python3

    # arr[]: Input Array
    # N : Size of the Array arr[]
    # Function to count inversions in the array.
    def merge(self, arr, low, mid, high):
        l = low
        r = mid + 1
        temp = []
        while l <= mid and r <= high:
            if arr[l] <= arr[r]:
                temp.append(arr[l])
                l += 1
            else:
                self.count += mid + 1 - l
                temp.append(arr[r])
                r += 1
        while l <= mid:
            temp.append(arr[l])
            l += 1
        while r <= high:
            temp.append(arr[r])
            r += 1
        arr[low : high + 1] = temp[:]

    def mergesort(self, arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergesort(arr, low, mid)
        self.mergesort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)

    def inversionCount(self, arr, n):
        self.mergesort(arr, 0, n - 1)
        return self.count


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a, n))
# } Driver Code Ends
