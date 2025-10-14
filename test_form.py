import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Selenium Manager will auto-download the appropriate driver
    options = Options()
    options.add_argument("–headless")  # run without UI
    options.add_argument("–no-sandbox")  # required in many CI environments
    options.add_argument("–disable-dev-shm-usage")  # overcome limited /dev/shm size on Linux

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_successful_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    text_input = driver.find_element(By.ID, 'username')
    text_input.clear()
    text_input.send_keys('tomsmith')

    text_input = driver.find_element(By.ID, 'password')
    text_input.clear()
    text_input.send_keys('SuperSecretPassword!')

    submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

    success_message = driver.find_element(By.CSS_SELECTOR, 'div.flash.success')
    assert "You logged into a secure area!" in success_message.text

def test_unsuccessful_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    text_input = driver.find_element(By.ID, 'username')
    text_input.clear()
    text_input.send_keys('username')

    text_input = driver.find_element(By.ID, 'password')
    text_input.clear()
    text_input.send_keys('password')

    submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

    unsuccess_message = driver.find_element(By.CSS_SELECTOR, 'div.flash.error')
    assert "Your username is invalid!" in unsuccess_message.text







