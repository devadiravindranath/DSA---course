def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return len(stack) == 0


s = input("Enter a string of brackets: ")

if isValid(s):
    print("Valid Parentheses")
else:
    print("Invalid Parentheses")