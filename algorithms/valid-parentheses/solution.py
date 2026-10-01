class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        st = []

        for i in s:

            # Opening bracket
            if i in bracket:
                st.append(i)

            # Closing bracket
            else:
                # No opening bracket available
                if len(st) == 0:
                    return False

                # Closing bracket doesn't match top opening bracket
                elif i != bracket[st[-1]]:
                    return False

                # Correct pair
                else:
                    st.pop()

        # Stack should be empty
        if len(st) == 0:
            return True
        else:
            return False