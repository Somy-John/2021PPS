class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        str_s = []
        for i in range(0, len(S)):
            char = S[i]
            print (char)
            if char != '#':
                str_s.append(char)
            else:
                if (len(str_s) > 0) :
                    str_s.pop()
                    
        str_t = []
        for i in range(0, len(T)):
            char = T[i]
            if char != '#':
                str_t.append(char)
            else:
                if (len(str_t) > 0) :            
                    str_t.pop()
    
        return str_s == str_t