from utils import *
from Randomization import *
from .componentRule import *

class Accordion:
    columnRule = ColumnRule()
    rowRule = RowRule()
    
    columnRule.singleColumn = True
    rowRule.firstRow = True
    rowRule.notFirstRow = True

    def __init__(self, id):
        self.token = "ACCORDIAN"

        self.id = id

        self.classes = [
            "accordion",
            "accordion accordion-flush"
        ]

        self.builder()

    def builder(self):
        self.num_items = AccordionRandom.get_num_items()

    def __add__(self, other):
        if isinstance(other, str):
            return other + self.html()

    def html(self):
        return """
        <div class="accordion" id="{}">
            {}
        </div>
        """.format(self.id, self.items_html())
    
    def items_html(self):
        html_string = ""
        for i in range(self.num_items):
            html_string += self.item_html(i+1, i==0)
        return html_string
    
    def item_html(self, idx, first=False):
        show = "show" if first else ""
        collapse_id = f"collapse-{self.id}_{idx}"
        return f"""
        <div class="accordion-item">
            <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#{collapse_id}" aria-expanded="true" aria-controls="{collapse_id}">
                    [] #{idx}
                </button>
            </h2>
            <div id="{collapse_id}" class="accordion-collapse collapse {show}" data-bs-parent="#{self.id}">
                <div class="accordion-body">
                    []
                </div>
            </div>
        </div>"""
    
    def traverse(self, tabs):
        print("\t" * tabs, end="")
        print(self.token+"|"+str(self.num_items))