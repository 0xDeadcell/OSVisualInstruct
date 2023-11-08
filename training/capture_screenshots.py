import subprocess
import os
import json
import time
import requests
from bs4 import BeautifulSoup
import pyautogui

def get_installed_applications(ps_script_path):
    try:
        # Run the PowerShell script to get installed applications
        result = subprocess.run(["powershell.exe", "-ExecutionPolicy", "Unrestricted", "-File", ps_script_path],
                                capture_output=True, text=True, check=True)
        # You'd need to process the result.stdout to extract the application list
        apps = []  # Replace this with actual parsing code
        return apps
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to get installed applications: {e}")
        return []

def run_application(app_path):
    try:
        # Run the application
        proc = subprocess.Popen(app_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return proc
    except Exception as e:
        print(f"An error occurred while trying to run application {app_path}: {e}")
        return None

def take_screenshot(app_name):
    time.sleep(5)  # Wait for the app to open
    # This will take a full-screen screenshot - you would need to focus and capture just the app window
    screenshot = pyautogui.screenshot()
    path = os.path.join(script_folder, app_name)
    if not os.path.exists(path):
        os.makedirs(path)
    screenshot.save(os.path.join(path, f"{app_name}.png"))
    return screenshot.size

def get_app_description(app_name):
    # Google's ToS does not allow scraping search results
    description = "Description not available."  # Placeholder for actual description
    return description

def save_details_json(app_name, app_path, screenshot_resolution, description):
    details = {
        "name": app_name,
        "path": app_path,
        "resolution": f"{screenshot_resolution[0]}x{screenshot_resolution[1]}",
        "description": description
    }
    with open(os.path.join(script_folder, app_name, "details.json"), "w") as f:
        json.dump(details, f, indent=4)

if __name__ == "__main__":
    script_folder = os.path.dirname(os.path.realpath(__file__))
    ps_script_path = os.path.join(script_folder, "Get-InstalledApplications.ps1")
    installed_apps = get_installed_applications(ps_script_path)

    for app in installed_apps:
        app_name = app['DisplayName']
        app_path = app['InstallLocation']
        if os.path.isfile(app_path):
            process = run_application(app_path)
            if process:
                resolution = take_screenshot(app_name)
                description = get_app_description(app_name)
                save_details_json(app_name, app_path, resolution, description)
                process.terminate()  # Be careful with terminating processes
