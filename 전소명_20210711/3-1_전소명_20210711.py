def checkRecord(s):
        if 'LLL' in s: return False
        elif s.count('A')>=2:return False
        else: return True