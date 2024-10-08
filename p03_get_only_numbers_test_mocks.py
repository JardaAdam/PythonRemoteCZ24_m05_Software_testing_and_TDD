from unittest.mock import patch, MagicMock
from p03_get_only_numbers import get_only_numbers, API


def test_read_only_numbers():

    #test_data = ["1,4,5,25,aa,bb,23,4", "324,24,234www,1,23", "545,3w,32"]
    test_data = open('bb').readlines()

    expected = "1|4|5|25|23|4|324|24|1|23|545|32"

    fake_api = MagicMock()
    fake_api.get_data_from_file.return_value = test_data  # get_data method mocking
    with patch('p03_get_only_numbers.API', fake_api):
        # patch replaces the original object and context manager defines the scope of use of the mock
        result = get_only_numbers()
        assert result == expected
