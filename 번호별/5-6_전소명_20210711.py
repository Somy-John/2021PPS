 def isPalindrome(self, s: str) -> bool:
        strList = list(''.join(char for char in s if   char.isalnum()).lower())
        center = int(len(strList)/2)
        if len(strList)==1: return True;
        elif strList[0:center] == list(reversed(strList[-center:])) :
            return True
        else : return False