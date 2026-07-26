class Solution:
    def isValid(self, s: str) -> bool:
        close = set([")","}","]"])
        st = []
        i=0
        while i<len(s):
            if s[i] in close:
                if len(st)<=0:
                    return False
                last = st.pop()
                if not ((s[i]==")" and last=="(") or (s[i]=="]" and last=="[") or (s[i]=="}" and last=="{")):
                    return False
            else:
                st.append(s[i])
            i+=1
        if len(st)>0:
            return False
        return True
