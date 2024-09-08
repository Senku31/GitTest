import threading
from datetime import datetime
import pytest
from selenium import webdriver
from flaskblog import create_app
from werkzeug.serving import make_server

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope='session')
def client():
    app = create_app()
    yield app.test_client()


@pytest.fixture(scope='session')
def run_server():
    app = create_app()
    s = make_server("localhost", 5000, app)
    t = threading.Thread(target=s.serve_forever)
    yield t.start()
    s.shutdown()
    t.join()


@pytest.fixture(scope='function')
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        driver = webdriver.Ie()
    driver.maximize_window()
    driver.implicitly_wait(2)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extras', [])
    if report.when == 'call':
        extras.append(pytest_html.extras.url(driver.current_url))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            extras.append(pytest_html.extras.html("<div>Logs</div>"))
            file_name = report.nodeid.replace("::", "_") + ".png"
            file_name = f'./../reports/assets/{file_name}'
            _capture_screenshot(file_name)
            if file_name:
                html = f'<div><img src="{file_name}" alt="screenshot" style="width:304px;hight:228px;" ' \
                        'onclick="window.open(this.src)" align=right"/></div>'
                extras.append(pytest_html.extras.html(html))
                report.extras = extras

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    date = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    config.option.htmlpath = f"./../reports/report-{date}.html"

