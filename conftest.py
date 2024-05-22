import pytest
from selenium import webdriver
from dotenv import load_dotenv

import os

load_dotenv()


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    # use Chrome options for headless
    driver.maximize_window()

    email = os.getenv("NAME")
    password = os.getenv("PASSWORD")
    base_url = os.getenv("BASE_URL")
    driver.get(base_url)

    request.cls.driver = driver
    request.cls.email = email
    request.cls.password = password
    request.cls.base_url = base_url

    username = os.getenv("KATALONUSERNAME")
    katalon_password = os.getenv("KATALONPASSWORD")
    katalon_base_url = os.getenv("KATALON_BASE_URL")
    driver.get(katalon_base_url)

    request.cls.driver = driver
    request.cls.username = username
    request.cls.katalon_password = katalon_password
    request.cls.katalon_base_url = katalon_base_url

    #@pytest.fixture(scope="class")
    #def connect_to_db(request):
    #pass

    #@pytest.fixture(scope="class")
    #def connect_to_excel(request):
    #pass

    yield driver  # this is a signal to py interpreter -> means it tells the driver  to quit when nobody uses. it returns a driver
    driver.quit()
