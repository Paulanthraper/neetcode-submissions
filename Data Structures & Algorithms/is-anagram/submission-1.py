class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)>=len(t):
            for i in s:
                if s.count(i)!=t.count(i):
                    return False
                    break
                else:
                    pass
            return True
        if len(s)<=len(t):
            for i in t:
                if s.count(i)!=t.count(i):
                    return False
                    break
                else:
                    pass
            return True

            
            

        