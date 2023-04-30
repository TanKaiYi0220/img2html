from utils import *
from Randomization import *
from .componentRule import *

class Button:
    columnRule = ColumnRule()
    rowRule = RowRule()
    
    columnRule.singleColumn = True
    columnRule.doubleColumn = True
    columnRule.quadColumn = True
    rowRule.notFirstRow = True

    def __init__(self):
        self.token = "BUTTON"

        self.classes = [
            "btn btn-primary",
            "btn btn-secondary",
            "btn btn-success",
            "btn btn-danger",
            "btn btn-warning",
            "btn btn-info",
            "btn btn-light",
            "btn btn-dark",
            "btn btn-link"
        ]

        self.builder()

    def builder(self):
        self.class_idx = ButtonRandom.get_button_idx()        

    def __add__(self, other):
        if isinstance(other, str):
            return other + self.html()

    def html(self):
        return self.item_html()
    
    def item_html(self):
        return f"""<button type="button" class="{self.classes[self.class_idx]}">[]</button>"""
    
    def traverse(self, tabs):
        print("\t" * tabs, end="")
        print(self.token+"|"+self.classes[self.class_idx])