import pytest
from selenium import webdriver
from src.web_automation.gdrive_manager import init_driver
from config.constants import GDRIVE_URL

@pytest.fixture
def driver():
    driver = init_driver()
    yield driver
    driver.quit()

def test_gdrive_login(driver):
    """Verify successful loading of Google Drive."""
    driver.get(GDRIVE_URL)
    assert "Google Drive" in driver.title

# Run with:
# pytest tests/test_web.py -v