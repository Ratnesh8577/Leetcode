"""class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                # Pop until the matching '('
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()  # Remove the '('
                stack.extend(temp)  # Push reversed substring back
            else:
                stack.append(char)
        return ''.join(stack)
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        def helper(index):
            result = []
            while index < len(s):
                if s[index] == '(':
                    sub_str, index = helper(index + 1)
                    result.extend(reversed(sub_str))
                elif s[index] == ')':
                    return result, index
                else:
                    result.append(s[index])
                index += 1
            return result, index

        final_result, _ = helper(0)
        return ''.join(final_result)
