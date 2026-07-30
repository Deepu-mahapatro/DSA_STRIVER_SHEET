#REVERE SUBSTRING BETWEEN EACH PAIR OF PARENTHESIS 

class Solution:
    def reverseParentheses(self, s: str) -> str:

        # Stack stores the starting index of each '('
        stack = []

        # This list will store the characters of our answer
        result = []

        # Traverse each character in the string
        for ch in s:

            # If we find an opening bracket
            if ch == '(':

                # Save the current length of result.
                # This tells us where this substring starts.
                stack.append(len(result))

            # If we find a closing bracket
            elif ch == ')':

                # Get the matching '(' position
                start = stack.pop()

                # Reverse the substring from 'start' till the end
                result[start:] = result[start:][::-1]

            # Normal character
            else:

                # Add it to the result list
                result.append(ch)

        # Convert list into string
        return "".join(result)


# ---------------- Driver Code ----------------

solution = Solution()

# Test Case 1
s = "(abcd)"
print(solution.reverseParentheses(s))      # dcba

# Test Case 2
s = "(u(love)i)"
print(solution.reverseParentheses(s))      # iloveu

# Test Case 3
s = "(ed(et(oc))el)"
print(solution.reverseParentheses(s))      # leetcode

# Test Case 4
s = "a(bcdefghijkl(mno)p)q"
print(solution.reverseParentheses(s))      # apmnolkjihgfedcbq