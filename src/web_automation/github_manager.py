import requests
import base64
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
USER = os.getenv("GITHUB_USER")
PATH = os.getenv("DESKTOP_PATH", "~/Desktop")
REPO = "cua-automation-repo"

def run():
    if not TOKEN:
        print("❌ GITHUB_TOKEN not set. Please set it in environment variables.")
        return

    headers = {"Authorization": f"token {TOKEN}"}
    print("=== Connected to GitHub ===")

    # List files
    url = f"https://api.github.com/repos/{USER}/{REPO}/contents/{PATH}?ref=branch_name"

    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        print("📂 Files in repo:")
        for file in r.json():
            print("  📄", file["name"])
    else:
        print("❌ Failed to fetch files:", r.json())
        return

    # Upload / update test file
    file_path = "test_upload.txt"
    with open(file_path, "w") as f:
        f.write("Hello from CUA Automation via GitHub API!")

    with open(file_path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf-8")

    data = {
        "message": "Upload test file",
        "content": content
    }

    # Check if file exists
    get_url = f"https://api.github.com/repos/{USER}/{REPO}/contents/{file_path}"
    r_get = requests.get(get_url, headers=headers)
    if r_get.status_code == 200:
        data['sha'] = r_get.json()['sha']

    # Upload / update file
    upload_url = f"https://api.github.com/repos/{USER}/{REPO}/contents/{file_path}"
    r_put = requests.put(upload_url, headers=headers, json=data)
    if r_put.status_code in [200, 201]:
        print(f"✅ File '{file_path}' uploaded/updated successfully")
    else:
        print("❌ Upload failed:", r_put.json())
