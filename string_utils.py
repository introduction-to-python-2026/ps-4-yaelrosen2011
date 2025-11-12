def split_before_each_uppercases(formula):
    split_formula = []
    if len(formula) == 0:
        return []
    start = 0
    for end in range(1, len(formula)):
        if formula[end].isupper():
            split_formula.append(formula[start:end])
            start = end
    split_formula.append(formula[start:])
    return split_formula


def split_at_first_digit(formula):
    digit_location = 0
    for i, char in enumerate(formula):
        if char.isdigit():
            digit_location = i
            break
    
    if digit_location == 0: 
        return formula, 1
    else:
        prefix = formula[:digit_location]
        number = int(formula[digit_location:])
        return prefix, number

