import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "number, expected",
    [
        (7000792289606361, "7000 79** **** 6361"),
        (111111111, None),
        ("7000792289606361", "7000 79** **** 6361"),
        ("70007289606361", None),
        ("7158300734726758", "7158 30** **** 6758"),
        ("", None),
        (None, None),
    ],
)
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected
