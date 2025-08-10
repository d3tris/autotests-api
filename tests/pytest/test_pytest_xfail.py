import pytest


@pytest.mark.xfail(reason="A bug was found in the application due to which the test crashes with an error")
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason="The bug has already been fixed, but the test still has the xfail mark")
def test_without_bug():
    ...


@pytest.mark.xfail(reason="External service is temporarily unavailable")
def test_external_services_is_unavailable():
    ...
