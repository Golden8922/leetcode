class Solution:
    def isValid(self, s: str) -> bool:

        bracket = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        st = []

        for i in s:

            if i in bracket:
                st.append(i)

            else:
                if len(st) == 0:
                    return False

                if i != bracket[st[-1]]:
                    return False

                st.pop()

        return len(st) == 0