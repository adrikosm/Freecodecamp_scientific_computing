import re


def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first = ""
    second = ""
    lines = ""
    sumx = ""
    for item in problems:
        if re.search("[^\s0-9.+-]", item):
            if re.search("[/]", item) or re.search("[*]", item):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        first_number = item.split(" ")[0]
        operator = item.split(" ")[1]
        second_number = item.split(" ")[2]

        if len(first_number) >= 5 or len(second_number) >= 5:
            return "Error: Numbers cannot be more than four digits."

        sums = ""
        if operator == "+":
            sums = str(int(first_number) + int(second_number))
        elif operator == "-":
            sums = str(int(first_number) - int(second_number))

        length = max(len(first_number), len(second_number)) + 2
        top = str(first_number).rjust(length)
        bottom = operator + str(second_number).rjust(length - 1)
        line = ""
        res = str(sums).rjust(length)

        for s in range(length):
            line += "-"

        if item != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            first += top
            second += bottom
            lines += line
            sumx += res
    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines
    return string
