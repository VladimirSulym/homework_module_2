import pytest

from src.widget import mask_account_card, get_date


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


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2019-AS-03T18:35:29.512364", None),
        ("2019-0703T18:35:29.512364", None),
        ("2019-07-03T18:29.512364", "03.07.2019"),
        (None, None),
        (123123, None),
        (False, None),
        (True, None),
        ("EXECUTED", None),
    ],
)
def test_get_date(date, expected):
    assert get_date(date) == expected
