from utils import *
from .row import Row
from .col import Column
from Randomization import *
class Body:
    def __init__(self):
        self.token = "BODY"

        self.num_rows = [2, 3, 4, 5]

        self.builder()

    def builder(self):
        self.num_index = BodyRandom.get_num_index()
        self.num_row = self.num_rows[self.num_index]
        self.rows = [Row() for _ in range(self.num_row)]
        self.rows[0].isFirstRow = True

    def __str__(self):
        return self.token
    
    def html(self):
        rows_html = ""

        for row in self.rows:
            rows_html += row.html()

        return format_html(f"""<body>{rows_html}</body>""")
    
    def traverse(self, tabs=0):
        print("\t" * tabs, end="")
        print(self.token, end="")
        print("{")
        for content in self.rows:
            content.traverse(tabs+1)
        print("\t" * tabs, end="")
        print("}")

    def to_dsl(self, tabs):
        spacing = "\t" * tabs
        token = self.token
        content = [c.to_dsl(tabs+1) for c in self.rows]
        
        return spacing + token + "{\n" + "\n".join(content) + spacing + "}\n"