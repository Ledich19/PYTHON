# ex2
name = input('Enter your name? ')
print('Hello', name)
# ex3
result = 0
hours = input('Enter hours ? ')
rate = input('Enter rate? ')

def compute_pay(hours, rate):
  if int(hours) > 40:
    print("Overtime")
    result = (float(int(hours) - 40) * rate_fl * 1.5) + (40 * rate_fl  )
  else:
    print("Overtime")
    result = hours_fl * rate_fl  
  print("Pay: ", result)


try:
  hours_fl = float(hours)
  rate_fl = float(rate)
  compute_pay(hours_fl, rate_fl)
except:
  print("Error: please enter numeric input")
