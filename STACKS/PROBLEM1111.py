#MAXIMUM NESTING DEPTH OF TWO VALID PARENTHESIS 

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        # This list stores the final answer.
        # 0 means the parenthesis belongs to Group A.
        # 1 means the parenthesis belongs to Group B.
        result = []

        # Variable to keep track of the current nesting depth.
        depth = 0

        # Traverse each character in the given parentheses string.
        for ch in seq:

            # If we encounter an opening bracket,
            # we are entering one more nesting level.
            if ch == '(':
                depth += 1

                # Assign the current '(' based on whether
                # the depth is odd or even.
                #
                # Odd depth  -> Group 1
                # Even depth -> Group 0
                #
                # This alternates deep levels between two groups,
                # reducing the maximum depth of each group.
                result.append(depth % 2)

            # Otherwise, it is a closing bracket.
            else:
                # Assign ')' to the same group as its matching '('.
                # We use the current depth before decreasing it.
                result.append(depth % 2)

                # Leaving one nesting level.
                depth -= 1

        # Return the assignment array.
        return result


# ---------------- Driver Code ----------------

if __name__ == "__main__":
    obj = Solution()

    seq = "(()())"

    answer = obj.maxDepthAfterSplit(seq)

    print("Input :", seq)
    print("Output:", answer)