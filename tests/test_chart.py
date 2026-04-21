from utils.chart_utils import hover_and_get_mapped_data


def test_chart_data(chart_data):
    print("\nChart Data:", chart_data)

    assert chart_data is not None
    assert len(chart_data) > 0

    for item in chart_data:
        assert isinstance(item["year"], str)
        assert isinstance(item["value"], (int, float))


def test_chart_hover(chart_page):
    canvas = chart_page.get_canvas()

    hover_data = hover_and_get_mapped_data(chart_page.driver, canvas)

    print("\nFinal Hover Mapping:", hover_data)

    assert len(hover_data) > 0