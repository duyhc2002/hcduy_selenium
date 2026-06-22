import pytest


def test_navigation_back_and_forward(driver):
    """Verify browser navigation works from OrangeHRM homepage to Google and back."""
    assert "OrangeHRM" in driver.title

    driver.get("https://www.google.com")
    assert "Google" in driver.title

    driver.back()
    assert "OrangeHRM" in driver.title

    driver.forward()
    assert "Google" in driver.title
