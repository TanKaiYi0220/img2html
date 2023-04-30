from utils import *
from .col import Column

class Row:
    def __init__(self):
        self.token = "ROW"

        self.isFirstRow = False

        self.classes = [
            "row"
        ]

        self.cols = Column(isFirstRow=self.isFirstRow)

    def __str__(self):
        return self.token

    def html(self):
        content = self.cols.html() if self.cols else "{}"
        return format_html(f"""<div class="row">{content}</div>""")
    
    def traverse(self, tabs):
        print("\t" * tabs, end="")
        print(self.token, end="")
        print("{")
        self.cols.traverse(tabs+1)
        print("\t" * tabs, end="")
        print("}")