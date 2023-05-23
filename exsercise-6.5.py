str ='X-DSPAM-Confide nce: 0.8475'
string_start = str.find(':')
number = float(str[string_start + 1: ].strip())
print(number)