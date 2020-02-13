

def cal_gpa(grade_list, credit_list):
    sum_ = 0
    for ind in range(len(grade_list)):
        sum_ += grade_list[ind] * credit_list[ind]

    return sum_ / sum(credit_list)

if __name__ == "__main__":
    # all
    grade_list = [84, 72, 79, 90, 94, 87, 85, 82, 81, 80, 85, 80, 97, 91, 85, 81, 92, 93]
    credit_list = [2, 2, 3, 3, 3, 2, 1, 1, 1, 1, 1, 3, 2, 2, 1, 1, 1, 1]
    print(cal_gpa(grade_list, credit_list))

    # required
    grade_list = [84, 90, 94, 87, 85, 80, 97, 91, 81, 92, 93]
    credit_list = [2, 3, 3, 2, 1, 3, 2, 2, 1, 1, 1]
    print(cal_gpa(grade_list, credit_list))