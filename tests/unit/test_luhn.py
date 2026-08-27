import pytest

from creditcard import luhn


class TestLuhn:
    @pytest.mark.parametrize(
        "number,expected",
        [
            ("4539578763621486", True),
            ("5369835519963014", True),
            ("5369835519963013", False),
            ("30346836403940", True),
            ("6108000000000040", True),
            ("6108000000000041", False),
        ],
    )
    def test_check(self, number, expected):
        assert luhn.check(number) is expected

    @pytest.mark.parametrize(
        "number,expected",
        [
            ("6108000000000041", True),
            ("6108000000000040", False),
        ],
    )
    def test_check_softnex(self, number, expected):
        assert luhn.check_softnex(number) is expected
