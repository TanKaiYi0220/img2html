from Component import *
from Layout import *
from Randomization import *
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def screenshot(file_name):
    driver_path = r"C:\Users\xiaop\Desktop\Lab\Image-To-HTML\rule-based\chromedriver.exe"

    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    
    url = f"file:///{os.getcwd()}{file_name[1:]}"
    
    driver.get(url)
    
    time.sleep(1)

    # driver.set_window_size(1024, 600)
    # driver.maximize_window()

    # driver.fullscreen_window()

    # time.sleep(1)


    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    print(S('Width'), S('Height'))
    driver.set_window_size(S('Width'), S('Height')*2) # May need manual adjustment
    time.sleep(1)                                                                                                                
    driver.find_element_by_tag_name('body').screenshot(f'{file_name.replace("html", "png")}')

    driver.quit()


def generate_html(i):
    my_layout = Layout()

    ColumnRandom.reset()
    CardRandom.reset()

    my_layout.base.header.set_content(NavBar())

    for idx, r in enumerate(my_layout.base.body.rows):
        col_num = r.cols.col_num
        is_first_row = r.cols.isFirstRow
        components = [BodyComponentSet.getComponent(col_num=col_num, is_first_row=is_first_row) for i in range(col_num)]
        r.cols.set_content(components)

    soup = BeautifulSoup(my_layout.html(), 'html.parser')
    soup = soup.prettify()
    file_name = f".\\dataset\\html\\{i}.html"
    with open(file_name, "w", encoding = 'utf-8') as file:
        print(f"HTML write into {file_name}")
        file.write(str(soup))

    dsl = my_layout.to_dsl(0)
    dsl_file_name = file_name.replace("html", "dsl")
    with open(dsl_file_name, "w", encoding = 'utf-8') as file:
        print(f"DSL Write into {dsl_file_name}")
        file.write(str(dsl))

    screenshot(file_name=file_name)

    time.sleep(1)

if __name__ == "__main__":
    for i in range(1000):
        generate_html(i)