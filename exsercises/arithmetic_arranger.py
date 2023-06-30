def create_obj(example, solution):
  total_len = max(len(example[0]), len(example[2])) + 2
  obj = {}
  if len(example[0]) > len(example[2]):
    obj['operand1'] = '  ' + example[0]
    obj['operand2'] = example[1] + (total_len - len(example[2]) - 1) * ' ' + example[2]
  else:
    obj['operand1'] = (total_len - len(example[0])) * ' ' + example[0]
    obj['operand2'] = example[1] + ' ' + example[2]
  obj['line'] = '-' * total_len
  obj['solution'] = (total_len - len(str(solution))) * ' ' + str(solution)
  return obj

def solve_problem(example):
  operand1 = int(example[0])
  operand2 = int(example[2])
  if example[1] == '+':
    return operand1 + operand2
  elif example[1] == '-':
    return operand1 - operand2

def arithmetic_arranger(problems, is_solve=False):
  if len(problems) > 5:
    return 'Error: Too many problems.'
  
  problems_list = list()
  result = ['','','','']
    
  for example in problems:
    example = example.split()
    if example[1] != '+' and example[1] != '-':
      return "Error: Operator must be '+' or '-'."
    if len(example[0]) > 4 or len(example[2]) > 4:
      return "Error: Numbers cannot be more than four digits." 
    if not example[0].isdigit() or not example[2].isdigit():
      return "Error: Numbers must only contain digits."

    solution = solve_problem(example)
    obj = create_obj(example, solution)
    problems_list.append(obj)
  
  count  = 0
  for example in problems_list:
    count += 1
    separator = ' ' * 4
    if count == len(problems): separator = '\n'

    result[0] += example['operand1'] + separator
    result[1] += example['operand2'] + separator
    result[2] += example['line'] + separator
    if is_solve == True:
      result[3] += example['solution'] + separator

  arranged_problems = ''
  for element in result:
    arranged_problems += element

  return arranged_problems.rstrip()


print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
