import pytest
# подробнее тут https://docs.pytest.org/en/latest/skipping.html#xfail-mark-test-functions-as-expected-to-fail
@pytest.mark.xfail(strict=True) 
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False