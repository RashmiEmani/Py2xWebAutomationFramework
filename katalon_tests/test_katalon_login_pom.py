import time

import allure
import pytest
from selenium import webdriver

from tests.page_objects.dashboard_page import DashboardPage
from tests.page_objects.login_page import LoginPage


# Assertions -> you can add here

class TestLogin:
    @allure.epic("VWO Login Test")
    @allure.feature("TC#0 - VWO App Negative Test")
    @pytest.mark.negative
    @pytest.mark.usefixtures("setup")
    def test_vwo_login_negative(self, setup):
        driver = setup
        driver.get(self.base_url)
        login_page = LoginPage(driver)
        login_page.login_to_vwo(email="admin@admin@gmail.com", password="admin")
        time.sleep(5)
        error_message = login_page.get_error_message_text()
        assert error_message == "Your email, password, IP address or location did not match"

    @allure.epic("VWO Login Test")
    @allure.feature("TC#1 - VWO App Positive Test")
    @pytest.mark.positive
    @pytest.mark.usefixtures("setup")
    def test_vwo_login_positive(self, setup):
        driver = setup
        driver.get(self.base_url)
        login_page = LoginPage(driver)
        login_page.login_to_vwo(email=self.email, password=self.password)
        time.sleep(10)
        dashboard_page = DashboardPage(driver)
        assert "Dashboard" in driver.title
        assert "Aman" in dashboard_page.user_logged_in_text()

# to run test case parallely(both positive and negative), use xdist
# syntax -> pytest -n auto tests/vwo_login_tests/test_vwo_login.py