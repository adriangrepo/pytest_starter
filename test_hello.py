from hello import more_hello, more_bye


def test_more_hello():
    assert "hi" == more_hello()


def test_bye():
    assert "bye" == more_bye()
