def arithmetic_arranger(problems, show_answers=False):
    first_line = []
    second_line = []
    dashes = []
    results = []

    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for problem in problems:
        # Determine operator
        if '+' in problem:
            operator = '+'
        elif '-' in problem:
            operator = '-'
        else:
            return "Error: Operator must be '+' or '-'."

        # Split problem into numbers and check if they are valid digits
        num1, num2 = problem.split(operator)
        num1, num2 = num1.strip(), num2.strip()

        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.' 

        width = max(len(num1), len(num2)) + 2

        if width > 6:
            return 'Error: Numbers cannot be more than four digits.'

        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width - 1))
        dashes.append('-' * width)

        if show_answers:
            result = str(eval(problem)).rjust(width)
            results.append(result)

    arranged_problems = '\n'.join([
        '    '.join(first_line),
        '    '.join(second_line),
        '    '.join(dashes)
    ])

    if show_answers:
        arranged_problems += '\n' + '    '.join(results)

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')