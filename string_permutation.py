def replace_question_mark(inp):
    out = []
    out.append(inp.replace('?', '0'))
    out.append(inp.replace('?', '1'))
    out.append(inp.replace('?', '0', 1).replace('?', '1'))
    out.append(inp.replace('?', '1', 1).replace('?', '0'))
    return out


print(replace_question_mark('ab?c?d?'))
