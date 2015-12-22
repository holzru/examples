def valid_parentheses(string):
    new = []
    check = []
    for char in string:
        if char == '(' or char == ')':
            new.append(char)
    for item in new:
        if item == '(':
            check.append(item)
        elif item == ')' and '(' in check:
            check.remove('(')
            print True
        else:
            print False
        print False


valid_parentheses("hi(hi)()")
valid_parentheses('hi())(')
