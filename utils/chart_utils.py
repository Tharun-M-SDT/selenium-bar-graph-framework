from selenium.webdriver.common.action_chains import ActionChains
import time


def hover_and_get_mapped_data(driver, canvas):
    actions = ActionChains(driver)

    # 🔥 Get chart info
    chart_info = driver.execute_script("""
        let chart = Chart.getChart(document.querySelector("#myChartMixed"));

        let labels = chart.data.labels;
        let values = chart.data.datasets[0].data;

        let result = [];

        for (let i = 0; i < labels.length; i++) {
            let year = labels[i];
            if (Array.isArray(year)) year = year[0];

            result.push({
                year: year,
                value: values[i]
            });
        }

        return result;
    """)

    width = canvas.size['width']
    height = canvas.size['height']

    step = int(width / len(chart_info))

    final_data = []

    for i, item in enumerate(chart_info):
        x = step * i + 20
        y = height // 2

        actions.move_to_element_with_offset(canvas, x, y).perform()
        time.sleep(0.5)

        print(f"Hovered → Year: {item['year']} | Value: {item['value']}")

        final_data.append(item)

    return final_data