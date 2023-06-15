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
    def allPairs(self, A, B, N, M, X):
        # map2 = {}
        ans = []
        # for i in range(M):
        #     if B[i] not in map2:
        #         map2[B[i]]=i
        for i in sorted(A):
            if X - i in B:
                ans.append((i, X - i))
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())

    while T > 0:
        sz = [int(x) for x in input().strip().split()]
        N, M, X = sz[0], sz[1], sz[2]
        A = [int(x) for x in input().strip().split()]
        B = [int(x) for x in input().strip().split()]
        ob = Solution()
        answer = ob.allPairs(A, B, N, M, X)
        sz = len(answer)

        if sz == 0:
            print(-1)

        else:
            for i in range(sz):
                if i == sz - 1:
                    print(*answer[i])
                else:
                    print(*answer[i], end=", ")

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
