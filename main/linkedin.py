from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
from selenium.webdriver import ActionChains
from random import randint

load_dotenv()

USER = os.getenv('EMAIL')
PASS = os.getenv('SENHA')
AREA = os.getenv('AREA')
MSG = os.getenv('MSG')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

driver.get("https://www.linkedin.com/feed/")



login = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, '//a[text()="Entrar"]')
    )
)

time.sleep(randint(1, 3))

login.click()

time.sleep(randint(3, 5))

email = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
        (By.ID, "username")
    )
)

email.send_keys(USER)

time.sleep(randint(1, 5))

senha = WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable(
        (By.ID, "password")
    )
)

senha.send_keys(PASS)

time.sleep(randint(1, 5))

entrar = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, '//button[text()="Entrar"]')
    )
)

time.sleep(randint(1, 5))

entrar.click()

time.sleep(15)

pesquisar = WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable(
        (By.CLASS_NAME, 'search-global-typeahead__input')
    )
)

pesquisar.send_keys(AREA)
pesquisar.send_keys(Keys.RETURN)

pessoas = WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable(
        (By.XPATH, '//button[text()="Pessoas"]')
    )
)

time.sleep(randint(1, 5))

pessoas.click()

time.sleep(randint(1, 5))

while True:
    ActionChains(driver)\
        .key_down(Keys.TAB)\
        .key_up(Keys.TAB)\
        .pause(randint(1, 2))\
        .key_down(Keys.TAB)\
        .key_up(Keys.TAB)\
        .pause(randint(1, 2))\
        .key_down(Keys.TAB)\
        .key_up(Keys.TAB)\
        .pause(randint(1, 2))\
        .key_down(Keys.RETURN)\
        .key_up(Keys.RETURN)\
        .perform()

    ActionChains(driver)\
        .key_down(Keys.TAB)\
        .key_up(Keys.TAB)\
        .pause(randint(1, 2))\
        .key_down(Keys.TAB)\
        .key_up(Keys.TAB)\
        .pause(randint(1, 2))\
        .key_down(Keys.RETURN)\
        .key_up(Keys.RETURN)\
        .perform()

    nota_msg = WebDriverWait(driver, 10). until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, '//textarea[@name="message"]')
        )
    )

    nota_msg.send_keys(MSG)

    ActionChains(driver)\
        .key_down(Keys.TAB)\
        .key_up(Keys.TAB)\
        .pause(randint(1, 2))\
        .key_down(Keys.TAB)\
        .key_up(Keys.TAB)\
        .pause(randint(1, 2))\
        .key_down(Keys.TAB)\
        .key_up(Keys.TAB)\
        .pause(randint(1, 2))\
        .key_down(Keys.RETURN)\
        .key_up(Keys.RETURN)\
        .perform()