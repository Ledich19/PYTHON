numbers_sum = 0
numbers_count = 0

while True:
  number = input('Enter your number: ')
  if number == 'done':
    break
  try:
    number = int(number)
  except:
    print('Invalid input')
    continue
  numbers_sum += number
  numbers_count += 1

print(numbers_sum, numbers_count, float(numbers_sum) / float(numbers_count))