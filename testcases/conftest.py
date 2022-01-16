import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import os
import sys
import time
import pytest_html
from datetime import datetime


@pytest.fixture(scope="class", autouse=True)
#set the url "url" fixture in setup params if you want it to be a commandline argument
def setup(request, browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager(log_level=20).install())

    url = "https://www.google.com/travel/"
    driver.get(url)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    #if you want to add more parsers (commandline-arguments) you can just add more parsers fx...
    #parser.addoption("--url")

#@pytest.fixture(scope="class", autouse=True)
#def url(request):
#    return request.config.getoption("--url")  


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")




def pytest_html_report_title(report):
    report.title = "Google Travel Automation Report"


'''
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        #always add url to report
        extra.append(pytest_html.extras.url("https://www.google.com/travel/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            #only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            # file_name = str(int(round(time.time() * 1000))) + ".png"
            file_name = report.nodeid.replace("::", "_") +".png"
            destinationFile = os.path.join(report_directory, file_name)
            feature_request = item.funcargs['request']
            driver = feature_request.getfixturevalue('setup')
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" onclick="window.open(this.src)" align="right"/></div>'%file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra

'''
