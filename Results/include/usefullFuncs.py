def check_input_data(desired_type, input_value):
    if type(desired_type) == str:
        return input_value

    num_is_less_than_null = False
    splited_list = input_value.split('-', 1)
    if len(splited_list) > 1:
        num_is_less_than_null = True
        input_value = splited_list[1]
    else:
        input_value = splited_list[0]
    if type(desired_type) == int:
        if input_value.isdigit():
            if num_is_less_than_null:
                return int(input_value) * -1
            return int(input_value)
    elif type(desired_type) == float:
        try:
            float(input_value)
        except ValueError:
            return False
        else:
            if num_is_less_than_null:
                return float(input_value) * -1
            return float(input_value)
    return False

