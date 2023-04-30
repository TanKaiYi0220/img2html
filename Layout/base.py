from utils import *

class Base:
    def __init__(self):
        self.token = "BASE"

        self.header = None
        self.body   = None
        self.footer = None

    def __str__(self):
        return self.token

    def html(self):
        header_html = self.header.html() if self.header else "{}"
        body_html   = self.body.html() if self.body else "{}"
        footer_html = self.footer.html() if self.footer else "{}"
        return format_html(f"""
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Bootstrap demo</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
                <link rel="stylesheet" type="text/css" href="./style.css">
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/js/bootstrap.bundle.min.js" integrity="sha384-qKXV1j0HvMUeCBQ+QVp7JcfGl760yU08IQ+GpUo5hlbpg51QRiuqHAJz8+BrxE/N" crossorigin="anonymous"></script>
            </head>
            {header_html}
            <body>
                {body_html}
            </body>
            {footer_html}
        </html>""")
    
    def traverse(self, tabs=0):
        print("\t" * tabs, end="")
        print(self.token, end="")
        print("{")
        self.header.traverse(tabs+1)
        self.body.traverse(tabs+1)
        self.footer.traverse(tabs+1)
        print("\t" * tabs, end="")
        print("}")