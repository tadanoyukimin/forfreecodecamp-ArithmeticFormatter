def arithmetic_arranger(problems, sums=False):
    sumlist = []
    spaces = '    '
    onespace = ' '
    row1 = row2 = row3 = ''
    dash = ''
    onedash = '-'
    if len(problems) > 5:
        return "Error: Too many problems."
#problems = ["32 + 698", "3801 - 2", "50 + 50", "123 - 49", "12 + 3600"]
    for problem in problems:
        splittedstring = problem.split()
        row1number = splittedstring[0]
        row2number = splittedstring[2]
        operator = splittedstring[1]
        try:
            if len(row1number) > 4 or len(row2number) > 4:
                raise Exception
        except:
            return "Error: Numbers cannot be more than four digits."

        try:
            int(row1number)
            int(row2number)
        except:
            return "Error: Numbers must only contain digits."

        try:
            if operator != '+' and operator != '-':
                raise Exception
        except:
            return "Error: Operator must be '+' or '-'."
        
        space = max(len(row1number), len(row2number))

        if not row1:
            row1 += row1number.rjust(space + 2)
            row2 += operator + onespace + row2number.rjust(space)
            dash += onedash * (space + 2)
        elif len(row1) > 1:
            row1 += row1number.rjust(space + 6)
            row2 += operator.rjust(5) + onespace + row2number.rjust(space)
            dash += spaces + onedash * (space + 2)
        if sums:
            sumlist.append(str(eval(problem)))
            for s in sumlist:
                splitsumlist = s.split()
                row3number = splitsumlist[0]
            if not row3:
                row3 += row3number.rjust(space + 2)
            else:
                row3 += row3number.rjust(space + 6)
    if sums:

        result = row1 + '\n' + row2 + '\n' + dash + '\n' + row3
    else:
        result = row1 + '\n' + row2 + '\n' + dash
    
    return result

    
        
print(arithmetic_arranger(["3234 + 698", "3801 - 222", "50 + 50", "123 - 49", "12 + 3600" ], True))  