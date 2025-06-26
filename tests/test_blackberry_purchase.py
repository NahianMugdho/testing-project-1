# test_blackberry_purchase.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_blackberry_purchase(driver):
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    for product in products:
        product_name = product.find_element(By.XPATH, ".//div/h4/a").text
        if product_name == "Blackberry":
            product.find_element(By.XPATH, "div[2]/button").click()
            break

    driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    driver.find_element(By.ID, "country").send_keys("bang")

    wait = WebDriverWait(driver, 7)
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Bangladesh')))
    driver.find_element(By.LINK_TEXT, "Bangladesh").click()
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    success_text = driver.find_element(By.CLASS_NAME, "alert-success").text
    driver.get_screenshot_as_file("screenshot.png")

    print(success_text)
    assert "Success" in success_text
