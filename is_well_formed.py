def is_well_formed(str):
    """ str: all characters in str are one of: '{','}','[',']','(',')'
    return true if all brackets are properly matched and ordered
    """
    stack = []
    for ch in str:
        if is_closing_br(ch):
            if not stack or not complements(stack[len(stack) - 1], ch):
                return False
            else:
                stack.pop()
        else:
            stack.append(ch)
    return not stack


def is_closing_br(bracket):
    closing_brackets = [')', '}', ']']
    return bracket in closing_brackets


def complements(br1, br2):
    compl_map = {'(': ')', '{': '}', '[': ']'}
    return compl_map[br1] == br2

tests = ['[]', '[{]}', '[{()()}[[]{}]]']

print([is_well_formed(tests[i]) for i in xrange(len(tests))])