class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            # If the current string is complete
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if we still have opens left
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add ')' if closes are valid
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result


# Example usage:
# sol = Solution()
# print(sol.generateParenthesis(3))
