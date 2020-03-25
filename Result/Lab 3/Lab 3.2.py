
def is_armstrong(your_number):
    your_number_string = str(your_number)
    number_len = len(your_number_string)
    num_power_sum = 0
    for one_digit_string in your_number_string:
        one_digit = int(one_digit_string)
        num_power_sum += one_digit ** number_len
    return num_power_sum == your_number
 
for i in range(10, 10000):
    if is_armstrong(i):
        print(i)
