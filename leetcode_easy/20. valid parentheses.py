class Solution:
 def isValid(self,s):
        
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {  ")" : "("  , "}" : "{"  , "]" : "[" }
        stack = []

        for char in s:
            if char in bracket_map:
                if len(stack) == 0 or stack.pop() != bracket_map[char]:
                  return False
              
                else: 
                    stack.append(char)

        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("]", False),
        ("(", False),
    ]

    for s, expected in test_cases:
        result = sol.isValid(s)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"String: {s:<8} | Expected: {str(expected):<5} | Got: {str(result):<5} | {status}")



            
     


