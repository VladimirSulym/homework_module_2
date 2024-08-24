from src.decorators import summ_my_int


def test_log(capsys):
    summ_my_int("1002", 2)
    captured = capsys.readouterr()
    assert captured.out == "summ_my_int error: TypeError. Inputs: ('1002', 2)\n"

    summ_my_int()
    captured = capsys.readouterr()
    assert captured.out == "summ_my_int error: TypeError. Inputs: ()\n"

    summ_my_int(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "summ_my_int ок\n"
