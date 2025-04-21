class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def getstack(ss):
            st=[]
            for i in range(len(ss)):
                if ss[i]!="#":
                    st.append(ss[i])
                else:
                    if st:
                        st.pop()

            return st

        return getstack(s) == getstack(t)
        