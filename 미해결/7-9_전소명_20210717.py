class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        while True:
            for i in range(len(s)):
                if s.find(s[i]*k)!=-1:
                    s = s.replace(s[i]*k,"")
                    break
            if i==len(s)-1: break
        return s

S = Solution()
print(S.removeDuplicates("deeedbbcccbdaa",3))