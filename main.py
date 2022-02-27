from random import randint


class Die:

    def __init__(self, num_side_4=4, num_side_6=6,
                 num_side_8=8, num_side_10=10,
                 num_side_12=12, num_side_20=20):

        self.num_side_4 = num_side_4
        self.num_side_6 = num_side_6
        self.num_side_8 = num_side_8
        self.num_side_10 = num_side_10
        self.num_side_12 = num_side_12
        self.num_side_20 = num_side_20

    def roll_die_4(self):
        return randint(1, self.num_side_4)

    def roll_die_6(self):
        return randint(1, self.num_side_6)

    def roll_die_8(self):
        return randint(1, self.num_side_8)

    def roll_die_10(self):
        return randint(1, self.num_side_10)

    def roll_die_12(self):
        return randint(1, self.num_side_12)

    def roll_die_20(self):
        return randint(1, self.num_side_20)
