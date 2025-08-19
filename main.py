from src.desktop_automation import folder_creator
from src.web_automation import gdrive_manager 
from src.web_automation import github_manager

if __name__ == "__main__":
    print("=== CUA Automation Project ===")
    print("1. Run Desktop Automation")
    print("2. Run Web Automation")
    print("3. Run GitHub Automation")   # ✅ now it shows option 3

    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        folder_creator.run()
    elif choice == "2":
        gdrive_manager.run()
    elif choice == "3":
        github_manager.run()    
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
