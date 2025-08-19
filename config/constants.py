# --- Desktop Automation Constants ---
DEFAULT_FOLDER_NAME = "CUA_Auto_Folder"
DESKTOP_PATH = "~/Desktop"  # Default save location

# --- Web Automation Constants (Google Drive) ---
GDRIVE_URL = "https://drive.google.com"
GDRIVE_NEW_BUTTON_XPATH = "//div[text()='New']"
GDRIVE_FOLDER_OPTION_XPATH = "//div[text()='Folder']"
GDRIVE_FOLDER_NAME_FIELD = "input[aria-label='Name']"

# --- Timing Constants ---
UI_LOAD_TIMEOUT = 10  # Seconds to wait for UI elements
CLICK_DELAY = 1       # Short pause between actions (anti-bot)

# --- Error Messages ---
FOLDER_EXISTS_ERROR = "Error: Folder already exists!"
LOGIN_FAILED_ERROR = "Google Drive login failed."