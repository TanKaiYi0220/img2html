from .accordion import *
from .button import *
from .card import *
from .carousel import *
import random

class BodyComponentSet:
    id = 0
    firstRowTokenPool = ["ACCORDIAN", "CAROUSEL", "BUTTON", "CARD"]
    notFirstRowTokenPool = ["ACCORDIAN", "BUTTON", "CARD"]

    singleColumnTokenPool = ["ACCORDIAN", "CAROUSEL"]
    doubleColumnTokenPool = ["BUTTON", "CARD"]
    quadColumnTokenPool = ["BUTTON", "CARD"]

    @classmethod
    def getComponent(cls, col_num, is_first_row):
        if col_num == 1:
            tokenPool = cls.singleColumnTokenPool
        elif col_num == 2:
            tokenPool = cls.doubleColumnTokenPool
        elif col_num == 4:
            tokenPool = cls.quadColumnTokenPool

        if is_first_row:
            tokenPool = list(set(tokenPool) & set(cls.firstRowTokenPool))
        else:
            tokenPool = list(set(tokenPool) & set(cls.notFirstRowTokenPool))
        token = random.choice(tokenPool)

        if token == "ACCORDIAN":
            cls.id += 1
            return Accordion(id=token+str(cls.id))
        elif token == "BUTTON":
            return Button()
        elif token == "CARD":
            return Card()
        elif token == "CAROUSEL":
            return Carousel(id=token+str(cls.id))