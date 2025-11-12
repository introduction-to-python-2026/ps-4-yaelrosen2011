def split_before_each_uppercases(formula):
    pass # Replace the `pass` with your code
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
    pass # Replace the `pass` with your code
    digit_location= 1
    for digit in formula[1:]:
        if digit.isdigit():
            break
    digit_location+=1
    
    if digit_location==len(formula):
        return formula,1
    else:
        prefix=formula[:digit_location]
        number=int(formula[digit_location:])
        return prefix,number
