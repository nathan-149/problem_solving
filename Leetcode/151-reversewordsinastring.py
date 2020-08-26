class Solution(object):
    def reverseWords(self, s):
        arr = s.split(" ")
        arr = filter(lambda x: (len(x) != 0), arr)
        print(arr)
        for i in range(len(arr) / 2):
            temp = arr[i]
            arr[i] = arr[len(arr) - 1 - i]
            arr[len(arr) - 1 - i] = temp

        ans = ""
        for i in range(len(arr)):
            ans += arr[i]
            if i < len(arr) - 1:
                ans += " "
        return ans

sol = Solution()
x = "  hello world!  "
print(sol.reverseWords(x))