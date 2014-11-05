def permutation(items, length):
    """
    Make a permutation list of certain length of the input list of strings.
    """
    if length <= 1:
        permutation_list = []
        for item in items:
            permutation_list += [[item]]
        return permutation_list
    permutation_list = []
    for first_item in range(len(items)):
        latter_lists = permutation(items[:first_item]+items[first_item+1:], length-1)
        for latter_list in latter_lists:
            permutation_list += [[items[first_item]] + latter_list]
    return permutation_list

def equation(numbers, symbols):
    """ Give lists of numbers and symbols and give out a equation. """
    if 'COMBINE' in symbols or 'DECIMAL' in symbols:
        for index in range(len(symbols)):
            if symbols[index] == 'COMBINE':
                return equation(combine(index, numbers),symbols[:index]+symbols[index+1:])
            if symbols[index] == 'DECIMAL':
                return equation(decimal(index, numbers),symbols[:index]+symbols[index+1:])
    else:
        result = []
        for index in range(len(symbols)):
            result+=[numbers[index]]
            result+=[symbols[index]]
        result+=[numbers[-1]]
        return result

def combine(index, numbers):
    """
    Combine figures.
    """
    item=numbers[index]+numbers[index+1]
    return numbers[:index]+[item]+numbers[index+2:]

def decimal(index, numbers):
    """
    Connect figures with a decimal point.
    """
    item=numbers[index]+'.'+numbers[index+1]
    return numbers[:index]+[item]+numbers[index+2:]

def delete_zeros(equation):
    """
    Delete zeros at the beginning of the strings of numbers.
    """
    index = 0
    while index < len(equation):
        if equation[index][0] == '0':
            equation[index] = equation [index][1:]
        else:
            index+=1
    return equation

def print_equation(equation):
    """
    Print an equation.
    """
    string = ''
    for item in equation:
        string += item
    print (string)

def advanced_computation():
    """
    Deal with EXP, SQRT and FACTORIAL computation.
    """

##print (permutation(['2', '0', '1', '8'], 4))
##print (permutation(['+', '-', '*', '/', 'COMBINE', 'DECIMAL'], 3))
##print (permutation(['EXP', 'SQRT', 'FACTORIAL'], 3))


##print (equation(['2','0','1','8'],['+','COMBINE','DECIMAL']))
##print (delete_zeros(['2', '+', '01.8']))
##print_equation(['2', '+', '1.8'])
