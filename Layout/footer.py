from utils import *
from .row import *

class Footer:
    def __init__(self):
        self.token = "FOOTER"

        self.num_rows = get_random_choice([1, 2, 3], [0.6, 0.3, 0.1])

        self.rows = [Row() for _ in range(self.num_rows)]

    def __str__(self):
        return self.token

    def html(self):
        return """<footer>{}</footer>"""
    
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