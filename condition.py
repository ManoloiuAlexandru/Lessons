qestion = input("Creat condition")
qestion = qestion.split()
sol = ''
if "nu" not in qestion:
    interv = list(qestion[-1])
    if interv[0] == '(' and interv[1] != '-':
        sol = sol + "(" + qestion[0] + '>' + interv[1] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<' + interv[3] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + interv[3] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<' + interv[3] + interv[4] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + interv[3] + interv[4] + ')'
    elif interv[0] == '(' and interv[1] == '-':
        sol = sol + "(" + qestion[0] + '>' + interv[1] + interv[2] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<' + interv[4] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + interv[4] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<' + interv[4] + interv[5] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + interv[4] + interv[5] + ')'
    elif interv[0] == '[' and interv[1] != '-':
        sol = sol + "(" + qestion[0] + '>=' + interv[1] + interv[2] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<' + interv[3] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + interv[3] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<' + interv[3] + interv[4] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + interv[3] + interv[4] + ')'
    elif interv[0] == '[' and interv[1] == '-':
        sol = sol + "(" + qestion[0] + '>=' + interv[1] + interv[2] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<' + interv[4] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + interv[4] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<' + interv[4] + interv[5] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + interv[4] + interv[5] + ')'
elif 'nu' in qestion:
    interv = list(qestion[-1])
    if interv[0] == '(' and interv[1] != '-':
        sol = sol + "(" + qestion[0] + '<=' + interv[1] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>=' + interv[3] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>' + interv[3] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>=' + interv[3] + interv[4] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>' + interv[3] + interv[4] + ')'
    elif interv[0] == '(' and interv[1] == '-':
        sol = sol + "(" + qestion[0] + '<=' + interv[1] + interv[2] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>=' + interv[4] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>' + interv[4] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>=' + interv[4] + interv[5] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>' + interv[4] + interv[5] + ')'
    elif interv[0] == '[' and interv[1] != '-':
        sol = sol + "(" + qestion[0] + '<=' + interv[1] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>=' + interv[3] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>' + interv[3] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>=' + interv[3] + interv[4] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>' + interv[3] + interv[4] + ')'
    elif interv[0] == '[' and interv[1] == '-':
        sol = sol + "(" + qestion[0] + '<=' + interv[1] + interv[2] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>=' + interv[4] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>' + interv[4] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>=' + interv[4] + interv[5] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>' + interv[4] + interv[5] + ')'
print(sol)
