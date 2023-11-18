import unittest
from datetime import datetime


def validate_symbol(symbol):
    return symbol.isupper() and 1 <= len(symbol) <= 7 and symbol.isalpha()


def validate_chart_type(chart_type):
    return chart_type in ["1", "2"]


def validate_time_series(time_series):
    return time_series in ["1", "2", "3", "4"]


def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


class TestStockVisualizerInputs(unittest.TestCase):
    def test_symbol(self):
        self.assertTrue(validate_symbol("AAPL"))
        self.assertFalse(validate_symbol("aapl"))
        self.assertFalse(validate_symbol("AAPL123"))
        self.assertFalse(validate_symbol("APPLEINC"))

    def test_chart_type(self):
        self.assertTrue(validate_chart_type("1"))
        self.assertTrue(validate_chart_type("2"))
        self.assertFalse(validate_chart_type("3"))
        self.assertFalse(validate_chart_type("A"))

    def test_time_series(self):
        self.assertTrue(validate_time_series("1"))
        self.assertTrue(validate_time_series("2"))
        self.assertTrue(validate_time_series("3"))
        self.assertTrue(validate_time_series("4"))
        self.assertFalse(validate_time_series("5"))
        self.assertFalse(validate_time_series("A"))

    def test_start_date(self):
        self.assertTrue(validate_date("2023-01-01"))
        self.assertFalse(validate_date("01-01-2023"))
        self.assertFalse(validate_date("2023/01/01"))
        self.assertFalse(validate_date("2023-13-01"))

    def test_end_date(self):
        self.assertTrue(validate_date("2023-12-31"))
        self.assertFalse(validate_date("31-12-2023"))
        self.assertFalse(validate_date("2023/12/31"))
        self.assertFalse(validate_date("2023-12-32"))


if __name__ == "__main__":
    unittest.main()
