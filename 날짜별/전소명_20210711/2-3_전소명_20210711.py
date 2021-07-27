def longestCommonPrefix(strs):
        rst = strs[0]
        print(rst)
        for currentStr in strs[1:]:
            tmp = ''
            for i in range(len(rst)):
                if i==len(currentStr): break
                elif currentStr[i] != rst[i]: break
                else: tmp += rst[i]
            rst = tmp
        return rst

longestCommonPrefix(["flower","flow","flight"])