import random


def get_random_code():
    code_list = []
    for i in range(10):
        code_list.append(str(i))

    random_num = random.sample(code_list, 6)
    code = ''.join(random_num)
    return code


if __name__ == '__main__':
    code = get_random_code()
    print(code)
