import pytest

from creditcard.card import CreditCard
from creditcard.exceptions import BrandNotFound


class TestCard:
    def test_is_valid(self):
        card = CreditCard("4539578763621486")
        assert card.is_valid() is True

        card = CreditCard("5369835519963014")
        assert card.is_valid() is True

        card = CreditCard("30346836403940")
        assert card.is_valid() is True

        card = CreditCard("00000000000001")
        assert card.is_valid() is False

        card = CreditCard("0000000000000a")
        assert card.is_valid() is False

    @pytest.mark.parametrize(
        "brand, number",
        [
            ("amex", "373257135458763"),
            ("aura", "5078601870000127985"),
            ("banese", "63611718700001275"),
            ("banese", "6374731870000127"),
            ("banese", "6374701870000127"),
            ("banese", "6366591870000127"),
            ("banese", "6374721870000127"),
            ("diners", "30346836403940"),
            ("elo", "5041756758046020"),
            ("hipercard", "6062825303833679"),
            ("softnex", "6108000000000000"),
            ("cabal", "6043240000000000"),
            ("master", "5369835519963014"),
            ("master", "5269116044687225"),
            ("master", "5899162511244726"),  # antigo maestro
            ("master", "5021316371000112"),  # antigo maestro
            ("master", "5930422341037703"),  # antigo maestro
            ("master", "6039137880232543"),  # antigo maestro
            ("master", "6063216106123345"),  # antigo maestro
            ("master", "6392403325708112"),  # antigo maestro
            ("codensa", "8700551111111111"),
            ("codensa", "5907121111111111"),
            ("codensa", "5294481111111111"),
            ("visa", "4539578763621486"),
        ],
    )
    def test_get_brand(self, brand, number):
        card = CreditCard(number)
        assert card.get_brand() == brand

    def test_get_brand_not_found(self):
        card = CreditCard("00000000000000")
        with pytest.raises(BrandNotFound) as err:
            card.get_brand()
        assert err.value.args[0] == "Card number does not match any brand"
