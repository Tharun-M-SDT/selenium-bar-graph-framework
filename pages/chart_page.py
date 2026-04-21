from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class ChartPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def wait_for_chart(self):
        WebDriverWait(self.driver, 20).until(
            lambda d: d.execute_script("""
                return typeof Chart !== 'undefined' &&
                       Chart.getChart(document.querySelector("#myChartMixed")) !== undefined;
            """)
        )

    def get_canvas(self):
        return self.driver.find_element(By.ID, "myChartMixed")