import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.chart_page import ChartPage


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def chart_page(driver):
    page = ChartPage(driver)
    page.open("https://chartjs-graph.webflow.io/")
    page.wait_for_chart()
    return page


@pytest.fixture(scope="function")
def chart_data(chart_page):
    driver = chart_page.driver

    data = driver.execute_script("""
        let chart = Chart.getChart(document.querySelector("#myChartMixed"));
        if (!chart) return null;

        let labels = chart.data.labels;
        let values = chart.data.datasets[0].data;

        let result = [];

        for (let i = 0; i < labels.length; i++) {
            let year = labels[i];

            if (Array.isArray(year)) {
                year = year[0];
            }

            result.push({
                year: year,
                value: values[i]
            });
        }

        return result;
    """)

    return data