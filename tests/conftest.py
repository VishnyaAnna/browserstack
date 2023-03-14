import allure
import pytest
from selene.support.shared import browser
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
from dotenv import load_dotenv


@pytest.fixture(scope="function", autouse=True)
def driver_config():
    load_dotenv()
    options = UiAutomator2Options().load_capabilities(
        {
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",

            "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",

            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-DEMO",
                "sessionName": "BStack first_test",

                "userName": "anna_MuQkz7",
                "accessKey": "Zqeos22HNxCaMmzzVtSJ"
            },
        }
    )

    with allure.step("Define driver"):
        browser.config.driver = webdriver.Remote(
            os.getenv("remote_url"), options=options
        )

    yield
