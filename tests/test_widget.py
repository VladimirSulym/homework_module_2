import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Platinum 700079228as06361", None),
        ("Visa Platinum 70007922806361", None),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 3538303347444SD95560", None),
        ("Счет 3538303347444951560", None),
        (None, None),
        (123123, None),
        (False, None),
        (True, None),
    ],
)
def test_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected
