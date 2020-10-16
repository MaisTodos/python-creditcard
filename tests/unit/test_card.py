from creditcard.card import CreditCard


class TestCard:
    def test_is_valid(self):
        card = CreditCard('4539578763621486')
        assert card.is_valid() is True

        card = CreditCard('5369835519963014')
        assert card.is_valid() is True

        card = CreditCard('30346836403940')
        assert card.is_valid() is True

        card = CreditCard('00000000000001')
        assert card.is_valid() is False

        card = CreditCard('0000000000000a')
        assert card.is_valid() is False
