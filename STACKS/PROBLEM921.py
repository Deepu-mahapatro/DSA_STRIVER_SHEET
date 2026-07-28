#MINIMUM ADD TO MAKE PARENTHESIS VALID 

class Solution:

    def minAddToMakeValid(self, s: str) -> int:

        # STORES THE NUMBER OF UNMATCHED OPENING BRACKETS '('
        open_count = 0

        # STORES HOW MANY PARENTHESES WE NEED TO ADD
        additions = 0

        # TRAVERSE EVERY CHARACTER IN THE STRING
        for ch in s:

            # IF THE CURRENT CHARACTER IS AN OPENING BRACKET
            if ch == '(':

                # STORE IT AS AN UNMATCHED OPENING BRACKET
                open_count += 1

            # IF THE CURRENT CHARACTER IS A CLOSING BRACKET
            else:

                # CHECK IF THERE IS AN OPENING BRACKET AVAILABLE
                if open_count > 0:

                    # MATCH THE CURRENT ')' WITH ONE '('
                    open_count -= 1

                # NO OPENING BRACKET IS AVAILABLE
                else:

                    # WE MUST ADD ONE '('
                    additions += 1

        # EVERY REMAINING '(' NEEDS ONE ')'
        additions += open_count

        # RETURN THE MINIMUM NUMBER OF ADDITIONS
        return additions


# CREATE OBJECT OF THE CLASS
obj = Solution()

# TAKE INPUT FROM THE USER
s = input("Enter Parentheses String: ")

# CALL THE FUNCTION
answer = obj.minAddToMakeValid(s)

# PRINT THE RESULT
print("Minimum Additions Required:", answer)