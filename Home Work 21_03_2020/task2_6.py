def check(NUM):
    check_help = True
    try:
        num_1 = float(NUM)
    except ValueError:
        print("Error, уведите целое или дробное число")
        check_help = False
    return check_help


def work():
    while 1:
        print("Уведите размеры щели:")
        len_slit = input("len_slit =  ")
        if check(len_slit) == False:
            continue
        height_slit = input("height_slit =  ")
        if check(height_slit) == False:
            continue

        # Параметры кирпича
        len_brick = input("len_brick =  ")
        if check(len_brick) == False:
            continue
        height_brick = input("height_brick =  ")
        if check(height_brick) == False:
            continue
        depth_brick = input("depth_brick =  ")
        if check(depth_brick) == False:
            continue
        else:
            slit_size = [len_slit, height_slit]
            brick_size = [len_brick, height_brick, depth_brick]

            if (max(slit_size) >= max(brick_size)) and (min(slit_size) >= min(brick_size)):
                print("Кирпичь войдет в щель")
            else:
                print("Кирпичь не войдет в щель")
        break


if __name__ == "__main__":
    work()
