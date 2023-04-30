from utils import *
from Randomization import *

class Column:
    def __init__(self, isFirstRow=False):
        self.token = "COLUMN"

        self.isFirstRow = isFirstRow

        self.classes = [
            "col-lg-12",
            "col-lg-6",
            "col-lg-3"
        ]

        self.col_nums = [1, 2, 4]

        self.builder()

    def builder(self):
        self.col_index = ColumnRandom.get_col_index()
        self.col_num = self.col_nums[self.col_index]
        self.col_class = self.classes[self.col_index]
        self.content = [None for _ in range(self.col_num)]

    def __str__(self):
        return self.token

    def html(self):
        col_html = ""
        for content in self.content:
            _content = content.html() if content else "{}" 
            col_html += f"""<div class="{self.classes[self.col_index]}">{_content}</div>"""
        
        return format_html(col_html)
    
    def set_content(self, content):
        self.content = content

    def traverse(self, tabs):
        print("\t" * tabs, end="")
        print(self.token+"|"+str(self.col_num), end="")
        print("{")
        for content in self.content:
            if content != None:
                content.traverse(tabs+1)
        print("\t" * tabs, end="")
        print("}")