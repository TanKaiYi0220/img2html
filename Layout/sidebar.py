class Sidebar:
    def __init__(self):
        self.token = "SIDEBAR"

    def __str__(self):
        return self.token

    def html(self):
        return """<div>{}</div>{}"""
    
    def set_content(self, content):
        return self.html().replace('{}', content)