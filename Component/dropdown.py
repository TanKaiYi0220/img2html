from utils import *
from Randomization import *

class Dropdown:
    def __init__(self):
        self.token = "DROPDOWN"

        self.button_classes = [
            "btn btn-primary dropdown-toggle",
            "btn btn-secondary dropdown-toggle"
        ]

        self.builder()

    def builder(self):
        self.button_class_idx = DropdownRandom.get_button_idx()

    def __add__(self, other):
        if isinstance(other, str):
            return other + self.html()

    def html(self):
        return f"""
        <div class="dropdown">
            <button class="{self.button_classes[self.button_class_idx]}" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                []
            </button>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#">Action</a></li>
                    <li><a class="dropdown-item" href="#">Another action</a></li>
                    <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
        </div>"""
        
    def traverse(self, tabs):
        print("\t" * tabs, end="")
        print(self.token+"|"+self.button_classes[self.button_class_idx])