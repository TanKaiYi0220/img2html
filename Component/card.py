from utils import *
from Randomization import *
from .componentRule import *

class Card:
    columnRule = ColumnRule()
    rowRule = RowRule()
    columnRule.doubleColumn = True
    columnRule.quadColumn = True
    rowRule.notFirstRow = True

    def __init__(self):
        self.token = "CARD"
        
        self.classes = [
            "card header-body-button",
            "card img-body-button",
            "card header-body",
            "card img-body"
        ]

        self.button_classes = [
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
        self.class_idx = CardRandom.get_card_idx()
        self.button_class_idx = CardRandom.get_button_idx()

        self.include_img = True if self.class_idx % 2 == 1 else False
        self.include_header = True if not self.include_img else False
        self.include_body = True
        self.include_button = True if self.class_idx < 2 else False

    def __add__(self, other):
        if isinstance(other, str):
            return other + self.html()

    def html(self):
        header_html = self.header_html() if self.include_header else ""
        img_html = self.img_html() if self.include_img else ""
        body_html = self.body_html() if self.include_body else ""
        return f"""
        <div class="card">
            {header_html}
            {img_html}
            {body_html}
        </div>"""
    
    def header_html(self):
        return f"""
        <div class="card-header" >
            []
        </div>"""
    
    def img_html(self):
        return f"""
        <svg class="bd-placeholder-img bd-placeholder-img-lg d-block w-100" width="800" height="200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: First slide" preserveAspectRatio="xMidYMid slice" focusable="false">
            <title>Placeholder</title>
            <rect width="100%" height="100%" fill="#777"></rect>
            <text x="50%" y="50%" fill="#555" dy=".3em"></text>
        </svg>"""

    def body_html(self):
        button_html = self.button_html() if self.include_button else ""
        return f"""
        <div class="card-body">
            <h5 class="card-title">[]</h5>
            <p class="card-text">[]</p>
            {button_html}
        </div>"""
    
    def button_html(self):
        return """<a href="#" class="{self.button_classes[self.button_class_idx]}">[]</a>"""
    
    def traverse(self, tabs):
        print("\t" * tabs, end="")
        print(self.token+"|"+self.classes[self.class_idx]+"|"+self.button_classes[self.button_class_idx])

    def to_dsl(self, tabs):
        spacing = "\t" * tabs
        token = self.token + "|" + self.classes[self.class_idx] + "|" + self.button_classes[self.button_class_idx]

        return spacing + token + "\n"