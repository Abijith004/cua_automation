import pytest
import os
import shutil
from pathlib import Path
from unittest.mock import patch, MagicMock
from src.desktop_automation.folder_creator import create_folder
from src.desktop_automation.file_organizer import organize_files_by_extension
from config.constants import DEFAULT_FOLDER_NAME, DESKTOP_PATH

# --------------------------
# Fixtures (Test Setup)
# --------------------------
@pytest.fixture
def clean_desktop():
    """Ensure test folder is deleted before/after each test."""
    test_folder = Path(DESKTOP_PATH) / DEFAULT_FOLDER_NAME
    if test_folder.exists():
        shutil.rmtree(test_folder)
    yield
    if test_folder.exists():
        shutil.rmtree(test_folder)

# --------------------------
# Tests for folder_creator.py
# --------------------------
def test_folder_creation(clean_desktop):
    """Verify folder is created correctly."""
    folder_path = create_folder(DEFAULT_FOLDER_NAME)
    
    assert Path(folder_path).exists()
    assert DEFAULT_FOLDER_NAME in os.listdir(DESKTOP_PATH)

def test_existing_folder_handling(clean_desktop):
    """Test no error when folder exists (exist_ok=True)."""
    create_folder(DEFAULT_FOLDER_NAME)
    # Should not raise FileExistsError
    create_folder(DEFAULT_FOLDER_NAME)  

# --------------------------
# Tests for file_organizer.py
# --------------------------
@pytest.fixture
def sample_files(tmp_path):
    """Create test files with different extensions."""
    files = {
        "test1.txt": "Sample text",
        "test2.pdf": b"PDF dummy data",
        "test3.jpg": b"JPEG dummy data"
    }
    for name, content in files.items():
        path = tmp_path / name
        if isinstance(content, str):
            path.write_text(content)
        else:
            path.write_bytes(content)
    return tmp_path

def test_file_organization(sample_files, monkeypatch):
    """Verify files are sorted into extension-named folders."""
    # Mock DESKTOP_PATH to use temp dir
    monkeypatch.setattr('config.constants.DESKTOP_PATH', str(sample_files))
    
    organize_files_by_extension()
    
    assert (sample_files / "txt").exists()
    assert (sample_files / "pdf").exists()
    assert "test1.txt" in os.listdir(sample_files / "txt")

# --------------------------
# Mocked PyAutoGUI Tests
# --------------------------
@patch('pyautogui.hotkey')
@patch('pyautogui.doubleClick')
def test_folder_open_gui(mock_double_click, mock_hotkey):
    """Test GUI interactions without real mouse movements."""
    from src.desktop_automation.folder_creator import open_folder
    open_folder(x=100, y=100)
    
    mock_hotkey.assert_called_once_with("win", "d")
    mock_double_click.assert_called_once_with(x=100, y=100)