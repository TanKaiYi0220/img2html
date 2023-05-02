from Component import *
from Layout import *
from bs4 import BeautifulSoup

if __name__ == "__main__":
    my_layout = Layout()

    my_layout.base.header.set_content(NavBar())

    for idx, r in enumerate(my_layout.base.body.rows):
        col_num = r.cols.col_num
        is_first_row = r.cols.isFirstRow
        components = [BodyComponentSet.getComponent(col_num=col_num, is_first_row=is_first_row) for i in range(col_num)]
        r.cols.set_content(components)

    soup = BeautifulSoup(my_layout.html(), 'html.parser')
    soup = soup.prettify()
    print(soup)
    with open("output.html", "w", encoding = 'utf-8') as file:
        file.write(str(soup))
        
    print(my_layout.traverse(0))

    dsl = my_layout.to_dsl(0)

    print(dsl)