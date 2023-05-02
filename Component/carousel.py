from utils import *
from Randomization import *
from .componentRule import *

class Carousel:
    columnRule = ColumnRule()
    rowRule = RowRule()
    
    columnRule.singleColumn = True
    rowRule.firstRow = True

    def __init__(self, id):
        self.token = "CAROUSEL"

        self.classes = [
            "carousel slide",
            "carousel slide carousel-fade"
        ]

        self.id = id

        self.builder()

    def builder(self):
        self.class_idx = CarouselRandom.get_carousel_idx()

    def __add__(self, other):
        if isinstance(other, str):
            return other + self.html()

    def html(self):
        return f"""
        <div id="{self.id}" class="{self.classes[self.class_idx]}">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <svg class="bd-placeholder-img bd-placeholder-img-lg d-block w-100" width="800" height="400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: First slide" preserveAspectRatio="xMidYMid slice" focusable="false">
                        <title>Placeholder</title>
                        <rect width="100%" height="100%" fill="#777"></rect>
                        <text x="50%" y="50%" fill="#555" dy=".3em">First Slide</text>
                    </svg>
                </div>
                <div class="carousel-item">
                    <svg class="bd-placeholder-img bd-placeholder-img-lg d-block w-100" width="800" height="400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Second slide" preserveAspectRatio="xMidYMid slice" focusable="false">
                        <title>Placeholder</title>
                        <rect width="100%" height="100%" fill="#666"></rect>
                        <text x="50%" y="50%" fill="#444" dy=".3em">Second slide</text>
                    </svg>
                </div>
                <div class="carousel-item">
                    <svg class="bd-placeholder-img bd-placeholder-img-lg d-block w-100" width="800" height="400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Third slide" preserveAspectRatio="xMidYMid slice" focusable="false">
                        <title>Placeholder</title>
                        <rect width="100%" height="100%" fill="#555"></rect>
                        <text x="50%" y="50%" fill="#333" dy=".3em">Third slide</text>
                    </svg>
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#{self.id}" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#{self.id}" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>"""
    
    def traverse(self, tabs):
        print("\t" * tabs, end="")
        print(self.token+"|"+self.classes[self.class_idx])

    def to_dsl(self, tabs):
        spacing = "\t" * tabs
        token = self.token + "|" + self.classes[self.class_idx]
        
        return spacing + token + "\n"