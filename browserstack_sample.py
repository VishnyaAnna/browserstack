from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

options = UiAutomator2Options().load_capabilities({
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
    }
})

browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")
browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))

browser.quit()
