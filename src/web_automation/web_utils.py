from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.constants import UI_LOAD_TIMEOUT
from utils.logger import setup_logger

logger = setup_logger(__name__)

def wait_for_element(driver, locator, timeout=UI_LOAD_TIMEOUT):
    """Generic wait-for-element helper."""
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    except TimeoutException:
        logger.error(f"Element not found: {locator}")
        raise

def safe_click(driver, locator):
    """Click with built-in error handling."""
    element = wait_for_element(driver, locator)
    element.click()
    logger.debug(f"Clicked: {locator}")

# Example usage in gdrive_manager.py:
# from web_utils import safe_click
# safe_click(driver, (By.XPATH, GDRIVE_NEW_BUTTON_XPATH))