quiz = [100, 100, 100]


def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg


print("The average is", cal_average(quiz))
