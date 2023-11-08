import subprocess
import os
import json
import time

def get_installed_applications(ps_script_path):
    try:
        result = subprocess.run(
            ["powershell.exe", "-ExecutionPolicy", "Unrestricted", "-File", ps_script_path],
            capture_output=True, text=True, check=True)
        apps = json.loads(result.stdout)  # Assuming the PowerShell script outputs JSON
        return apps
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to get installed applications: {e}")
        return []

def run_application(app_path, ps_start_process_script_path):
    try:
        # Run the PowerShell script to start the application and get the output
        result = subprocess.run(
            ["powershell.exe", "-ExecutionPolicy", "Unrestricted", "-File", ps_start_process_script_path, app_path],
            capture_output=True, text=True, check=True)
        process_info = json.loads(result.stdout)  # Assuming the PowerShell script outputs JSON with process ID
        return process_info['ProcessId']
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to run application {app_path}: {e}")
        return None

def take_screenshot(process_id, app_name, ps_get_screenshot_script_path):
    try:
        screenshot_path = os.path.join(script_folder, app_name, f"{app_name}.png")
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        subprocess.run(
            ["powershell.exe", "-ExecutionPolicy", "Unrestricted", "-File", ps_get_screenshot_script_path, "-processid", str(process_id), "-save_path", screenshot_path],
            check=True)
        return screenshot_path
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to take a screenshot for {app_name}: {e}")
        return None

def save_details_json(app_name, app_path, screenshot_path, description):
    details = {
        "name": app_name,
        "path": app_path,
        "screenshot": screenshot_path,
        "description": description
    }
    with open(os.path.join(script_folder, app_name, "details.json"), "w") as f:
        json.dump(details, f, indent=4)

if __name__ == "__main__":
    script_folder = os.path.dirname(os.path.realpath(__file__))
    ps_installed_apps_script_path = os.path.join(script_folder, "Get-InstalledApplications.ps1")
    ps_start_process_script_path = os.path.join(script_folder, "Start-ProcessGetOutput.psm1")
    ps_get_screenshot_script_path = os.path.join(script_folder, "Get-Screenshot.psm1")
    
    installed_apps = get_installed_applications(ps_installed_apps_script_path)

    for app in installed_apps:
        app_name = app['DisplayName']
        app_path = app['InstallLocation']
        
        if os.path.isfile(app_path):
            process_id = run_application(app_path, ps_start_process_script_path)
            if process_id:
                time.sleep(5)  # Wait for the app to initialize
                screenshot_path = take_screenshot(process_id, app_name, ps_get_screenshot_script_path)
                description = "Description not available"  # Replace this with actual description fetching logic
                save_details_json(app_name, app_path, screenshot_path, description)
                # Terminate the process if necessary. Use with caution!
                # subprocess.run(["taskkill", "/PID", str(process_id), "/F"])
