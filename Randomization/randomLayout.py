import random

class LayoutRandom:
    layout_index = [i for i in range(3)]
    layout_weights = [0.3, 0.3, 0.4]

    @classmethod
    def get_layout_index(cls):
        num = random.choices(cls.layout_index, weights=cls.layout_weights)[0]
        return num

class BodyRandom:
    num_index = [i for i in range(4)]
    num_weights = [0.4, 0.3, 0.2, 0.1]

    @classmethod
    def get_num_index(cls):
        num = random.choices(cls.num_index, weights=cls.num_weights)[0]
        return num

class ColumnRandom:
    col_index = [i for i in range(3)]
    col_weights = [0.5, 0.3, 0.2]

    @classmethod
    def get_col_index(cls):
        num = random.choices(cls.col_index, weights=cls.col_weights)[0]
        cls.col_weights = [0.2, 0.5, 0.3]
        return num
    
    @classmethod
    def reset(cls):
        cls.col_weights = [0.5, 0.3, 0.2]