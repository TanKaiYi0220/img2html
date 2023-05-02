from utils import *
from Randomization import *

class NavBar:
    def __init__(self):
        self.token = "NAVBAR"

        self.classes = [
            "navbar brand_text-dropdown-search",
            "navbar brand_text-dropdown",
            "navbar brand_text-search",
            "navbar dropdown-search",
            "navbar brand_text",
            "navbar dropdown",
            "navbar search",
        ]

        self.item_nums = [1, 2, 3, 4]

        self.builder()

    def builder(self):
        self.navbar_idx = NavBarRandom.get_navbar_idx()
        self.navbar_class = self.classes[self.navbar_idx]

        self.item_num_idx = NavBarRandom.get_item_idx()
        self.item_num = self.item_nums[self.item_num_idx]

        self.include_brand_text = True if "brand_text" in self.navbar_class else False
        self.include_dropdown = True if "dropdown" in self.navbar_class else False
        self.include_search = True if "search" in self.navbar_class else False

    def __add__(self, other):
        if isinstance(other, str):
            return other + self.html()

    def html(self):
        brand_html = self.brand_html() if self.include_brand_text else ""
        item_html = self.item_html() * self.item_num
        dropdown_html = self.dropdown_html() if self.include_dropdown else ""
        search_html = self.search_html() if self.include_search else ""
        return f"""
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
                {brand_html}
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        {item_html}
                        {dropdown_html}
                    </ul>
                    {search_html}
                </div>
            </div>
        </nav>
        """
    
    def brand_html(self):
        return """
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>"""
    
    def item_html(self):
        return """
        <li class="nav-item">
          <a class="nav-link" href="#">[]</a>
        </li>"""
    
    def dropdown_html(self):
        return """
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                []
            </a>
            <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
        </li>"""
    
    def search_html(self):
        return """
        <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
        </form>"""
    
    def traverse(self, tabs):
        print("\t" * tabs, end="")
        print(self.token+"|"+self.classes[self.navbar_idx]+"|"+str(self.item_num))

    def to_dsl(self, tabs):
        spacing = "\t" * tabs
        token = self.token + "|" + self.classes[self.navbar_idx] + "|" + str(self.item_num)
        
        return spacing + token + "\n"