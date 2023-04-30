class Header:
    def __init__(self):
        self.token = "HEADER"

        self.content = None

    def __str__(self):
        return self.token

    def html(self):
        content = self.content.html() if self.content else "{}"
        return f"""<header>{content}</header>"""
    
    def set_content(self, content):
        self.content = content

    def traverse(self, tabs=0):
        print("\t" * tabs, end="")
        print(self.token, end="")
        print("{")
        self.content.traverse(tabs+1)
        print("\t" * tabs, end="")
        print("}")