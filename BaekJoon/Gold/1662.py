s = input()

stack = []
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    elif s[i] == ')':
        count = 0
        while True:
            tmp = stack.pop()
            if tmp == '(':
                break
            count += tmp
        stack.append(int(stack.pop())*count)
    elif i < len(s)-1 and s[i+1] == '(':
        stack.append(int(s[i]))
    else:
        stack.append(1)

print(sum(stack))