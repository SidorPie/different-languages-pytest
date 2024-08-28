from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def is_element_present(browser, selector, string):
    try:
        browser.find_element(selector, string)
    except NoSuchElementException:
        return False
    return True

def test_page_contains_add_to_basket_button(browser):
    browser.get(link)
    # time.sleep(30)
    assert is_element_present(browser, By.CSS_SELECTOR, ".btn-add-to-basket"), \
            "No 'add to basket' button"