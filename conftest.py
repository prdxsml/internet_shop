import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # Выбор браузера для теста
    parser.addoption('--browser_name', action='store', default=None, help="chrome")
    # Обработчик командной строки для выбора языка теста. Представлены все тестируемые локали.
    parser.addoption('--language', action='store', default='en', help='What language will we use for the test? Languages available for verification: ar = العربيّة, ca = català, cs = česky, da = dansk, de = Deutsch, en-gb = British English, el = Ελληνικά, es = español, fi = suomi, fr = français, it = italiano, ko = 한국어, nl = Nederlands, pl = polski, pt = Português, pt-br = Português Brasileiro, ro = Română, ru = Русский, sk = Slovensky, uk = Українська, zh-hans = 简体中文')


def language(request):
    return request.config.getoption("--language")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    browser_name == "chrome"
    print("\nstart chrome browser for test ...")
    browser = webdriver.Chrome()
    
    yield browser
    print("\nquit browser..")
    browser.quit()