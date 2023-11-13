from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# time.sleep(30)

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def find_add_to_basket_button(browser):
    browser.get(link)
    find_button = browser.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    find_button.click()
    print('Button finded:', find_button)
    assert find_button in None
time.sleep(30)