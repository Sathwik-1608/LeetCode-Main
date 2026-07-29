class Solution(object):
    def isValid(self, s):
        st=[]
        for i in range(len(s)):
            if len(st)>0:
                if s[i]==")" and st[-1] == "(":
                    st.pop()
                elif s[i]=="}" and st[-1] == "{":
                    st.pop()
                elif s[i]=="]" and st[-1] == "[":
                    st.pop()
                else:
                    st.append(s[i])
            else:
                st.append(s[i])
        if len(st)>0:
            return False
        else:
            return True