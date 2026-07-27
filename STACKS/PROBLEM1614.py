#MAXIMUM NESTING DEPTH OF THE PARENTHESIS

class Solution:
    def maxDepth(self, s: str) -> int:
        # TRACKS CURRENT NESTING LEVEL
        current_depth = 0

        # STORE MAXIMUM DEPTH FOUND
        max_depth = 0

        # TRAVERSE EVERY CHARACTER IN THE STRING
        for ch in s:

            # OPENING BRACKET -> GO ONE LEVEL DEEPER
            if ch == '(':
                current_depth += 1

                # UPDATE THE MAXIMUM DEPTH IF NEEDED
                max_depth = max(max_depth, current_depth)

            # CLOSING BRACKET -> COME BACK ONE LEVEL
            elif ch == ')':
                current_depth -= 1

        # RETURN THE DEEPEST NESTING LEVEL
        return max_depth


# ---------------- MAIN PROGRAM ----------------

# CREATE OBJECT OF SOLUTION CLASS
obj = Solution()

# TAKE INPUT FROM USER
s = input("Enter the string: ")

# CALL THE FUNCTION
answer = obj.maxDepth(s)

# PRINT THE RESULT
print("Maximum Nesting Depth:", answer)