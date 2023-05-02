from utils import *
from .header import *
from .footer import *
from .sidebar import *
from .base import *
from .body import *
from Randomization import *

class Layout:
    def __init__(self):
        self.token = "LAYOUT"
        self.classes = [
            "H-Sl-F", "H-Sr-F", "H-F"
        ]

        self.builder()

    def builder(self):
        self.layout_idx = LayoutRandom.get_layout_index()

        self.layout_class = self.classes[self.layout_idx]
        
        self.base    = Base()
        self.base.header = Header()
        self.base.body   = Body()
        self.base.footer = Footer()

    def __str__(self):
        return self.token
    
    def html(self):
        return format_html(f"""{self.base.html()}""")
    
    def traverse(self, tabs=0):
        print("\t" * tabs, end="")
        print(self.token, end="")
        print("{")
        self.base.traverse(tabs+1)
        print("\t" * tabs, end="")
        print("}")

    def to_dsl(self, tabs):
        spacing = "\t" * tabs
        token = self.token
        base = self.base.to_dsl(tabs+1)
        
        return spacing + token + "{\n" + base + spacing + "}\n"