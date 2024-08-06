import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path  # Используем chromedriver-py для получения пути к chromedriver

@pytest.fixture
def browser():
    # Инициализация драйвера Chrome с использованием chromedriver-py
    service = Service(binary_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Запуск в headless режиме для CI/CD
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=service, options=options)
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
