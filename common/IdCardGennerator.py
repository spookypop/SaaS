# 随机生成身份证号码
import random


class IdNumber:
    def __init__(self, id_number):
        super(IdNumber, self).__init__()
        self.id = id_number

    def get_check_digit(self):
        """通过身份证号获取校验码"""
        check_sum = 0
        for i in range(0, 17):
            check_sum += ((1 << (17 - i)) % 11) * int(self.id[i])
        check_digit = (12 - (check_sum % 11)) % 11
        return check_digit if check_digit < 10 else "X"

    @classmethod
    def generate_id(cls, sex=0):
        """ 随机生成身份证号，sex = 0表示女性，sex = 1表示男性 """

        # 随机生成一个区域码(6位数)
        id_number = "412826"
        # 限定出生日期范围(8位数)
        birth_days = "19780420"
        id_number += str(birth_days)
        # 顺序码(2位数)
        id_number += str(random.randint(10, 99))
        # 性别码(1位数)
        id_number += str(random.randrange(sex, 10, step=2))
        # 校验码(1位数)
        return id_number + str(cls(id_number).get_check_digit())


if __name__ == '__main__':
    print(IdNumber.generate_id())  # 随机生成身份证号
