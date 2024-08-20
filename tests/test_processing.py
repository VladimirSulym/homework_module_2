from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(my_list_dict):
    assert filter_by_state(my_list_dict, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-20T02:08:58.425572"},
    ]

    assert filter_by_state(my_list_dict, None) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-20T02:08:58.425572"},
    ]

    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"date": "2018-11-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-13T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-08-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-20T02:08:58.425572"},
            ],
            "EXECUTED",
        )
        == None
    )

    assert filter_by_state(my_list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-20T02:08:58.425572"},
    ]

    assert filter_by_state(my_list_dict, "CANCELED") == [
        {"id": 615064591, "state": "CANCELED", "date": "2018-11-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-13T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-08-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    assert filter_by_state([], "CANCELED") == None
    assert filter_by_state([], None) == None
    assert filter_by_state(None, "CANCELED") == None
    assert filter_by_state(my_list_dict, 1) == None
    assert filter_by_state(my_list_dict, "abc") == None
