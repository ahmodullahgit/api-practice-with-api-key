import function_file

addition = function_file.add(1, 4, 5, 6, 7)
print(addition)

subtraction = function_file.sub(50,33)
print(subtraction)

multiplication = function_file.multiply(3, 4, 6)
print(multiplication)

division = function_file.devide(56, 9)
print(round(division, 2))

from function_file import add

addition_ = add(3, 4,5, 6, 8)
print(addition_)

from function_file import sub

subtraction_ = sub(46, 12)
print(subtraction_)

from function_file import multiply

multiplication_ = multiply(3, 4, 7)
print(multiplication_)

from function_file import devide

division_ = devide(12, 4)
print(division_)

from function_file import multiply as gun

usd = 354.65
exchange_rate = 103.765

bdt = gun(usd, exchange_rate)
print(f'Your Total Balance is {round(bdt)} Taka; from {usd} USD as {exchange_rate} taka per USD rate today.')
