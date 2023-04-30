from Component import *
from Layout import *
from bs4 import BeautifulSoup

START = f"""
<!doctype html>
  <html lang="en">
      <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>Bootstrap demo</title>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
          <link rel="stylesheet" type="text/css" href="./style.css">
          <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/js/bootstrap.bundle.min.js" integrity="sha384-qKXV1j0HvMUeCBQ+QVp7JcfGl760yU08IQ+GpUo5hlbpg51QRiuqHAJz8+BrxE/N" crossorigin="anonymous"></script>
      <body>
        {{}}
      </body>
  </html>"""

if __name__ == "__main__":
    my_accordion = Accordion(id="1")
    print(my_accordion)
    
    html = START.format(my_accordion.html())

    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.prettify()
    print(soup)
    with open("component_output.html", "w", encoding = 'utf-8') as file:
        file.write(str(soup))