from selenium.webdriver.common.by import By

class ChartLocators:
    CANVAS = (By.TAG_NAME, "canvas")

    # Update this based on actual DOM
    YEAR_LABELS = (By.XPATH, "//span[contains(text(),'20')]")

    # Tooltip (if exists in DOM)
    TOOLTIP = (By.CLASS_NAME, "chartjs-tooltip")