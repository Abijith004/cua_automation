# src/web_automation/gdrive_manager.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class GDriveManager:
    def __init__(self):
        self.driver = None

    def run(self):
        # Chrome will be installed automatically if not available
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

        # Example: open Google Drive
        self.driver.get("https://accounts.google.com/ServiceLogin?service=wise")
        self.driver.maximize_window()

        # keep browser open until closed manually
        input("Press Enter to quit...")
        self.driver.quit()


# ✅ Add a top-level function so main.py can call run() directly
def run():
    manager = GDriveManager()
    manager.run()


if __name__ == "__main__":
    run()
