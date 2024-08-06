import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    # Инициализация драйвера Chrome с использованием webdriver-manager
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

def test_yandex_search(browser):
    # Открытие страницы Яндекс
    browser.get('https://ya.ru')

    # Поиск элемента поиска и выполнение поиска
    search_box = browser.find_element('name', 'text')
    search_box.send_keys('pytest selenium')
    search_box.send_keys(Keys.RETURN)

    # Проверка наличия результатов
    assert 'pytest' in browser.title