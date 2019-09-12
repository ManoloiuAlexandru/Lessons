qestion = input("Creat condition")
qestion = qestion.split()
sol = ''
if "not" not in qestion:
    interv = list(qestion[-1])
    listnr = qestion[-1].replace('(', '').replace(')', '').replace('[', '').replace(']', '')
    listnr = listnr.split(',')
    if interv[0] == '(' and interv[1] != '-':
        sol = sol + "(" + qestion[0] + '>' + listnr[0] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + listnr[1] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + listnr[1] + ')'
    elif interv[0] == '(' and interv[1] == '-':
        sol = sol + "(" + qestion[0] + '>' + listnr[0] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + listnr[1] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + listnr[1] + ')'
    elif interv[0] == '[' and interv[1] != '-':
        sol = sol + "(" + qestion[0] + '>=' + listnr[0] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + listnr[1] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + listnr[1] + ')'
    elif interv[0] == '[' and interv[1] == '-':
        sol = sol + "(" + qestion[0] + '>=' + listnr[0] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + listnr[1] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '&&' + '(' + 'x' + '<=' + listnr[1] + ')'
elif 'not' in qestion:
    interv = list(qestion[-1])
    listnr = qestion[-1].replace('(', '').replace(')', '').replace('[', '').replace(']', '')
    listnr = listnr.split(',')
    if interv[0] == '(' and interv[1] != '-':
        sol = sol + "(" + qestion[0] + '<=' + listnr[0] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>=' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>' + listnr[1] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>=' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>' + listnr[1] + ')'
    elif interv[0] == '(' and interv[1] == '-':
        sol = sol + "(" + qestion[0] + '<=' + listnr[0] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>=' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>' + listnr[1] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>=' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>' + listnr[1] + ')'
    elif interv[0] == '[' and interv[1] != '-':
        sol = sol + "(" + qestion[0] + '<=' + listnr[0] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>=' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>' + listnr[1] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>=' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>' + listnr[1] + ')'
    elif interv[0] == '[' and interv[1] == '-':
        sol = sol + "(" + qestion[0] + '<=' + listnr[0] + ')'
        if interv[-1] == ')' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>=' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] != '-':
            sol = sol + '||' + '(' + 'x' + '>' + listnr[1] + ')'
        elif interv[-1] == ')' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>=' + listnr[1] + ')'
        elif interv[-1] == ']' and interv[-2] == '-':
            sol = sol + '||' + '(' + 'x' + '>' + listnr[1] + ')'
print(sol)
