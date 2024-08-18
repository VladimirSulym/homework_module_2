import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "number, expected",
    [
        (7000792289606361, "7000 79** **** 6361"),
        (111111111, None),
        ("7000792289606361", "7000 79** **** 6361"),
        ("70007289606361", None),
        ("7158300734726758", "7158 30** **** 6758"),
        ("71583ab734726758", None),
        ("", None),
        (None, None),
        (False, None),
        (True, None),
    ],
)
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (64686473678894779589, "**9589"),
        (111111111, None),
        ("35383033474447895560", "**5560"),
        ("70007289606361", None),
        ("7000ad89606361", None),
        ("", None),
        (None, None),
        (False, None),
        (True, None),
    ],
)
def test_get_mask_account(number, expected):
    assert get_mask_account(number) == expected
