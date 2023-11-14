# Download ssdeep, sigcheck, and handle to their respective folders
# ssdeep: For obtaining ssdeep fuzzy hashes (useful for finding similar files). You must extract the ssdeep ZIP file (available here) into a subfolder called “bin/ssdeep-2.14.1”.
# https://github.com/ssdeep-project/ssdeep/releases/download/release-2.14.1/ssdeep-2.14.1-win32-binary.zip
# Sysinternals Handle: For obtaining the open handles of a given process. You must place handle64.exe (available here) in a subfolder called “bin/sysinternals/handle”.
# https://download.sysinternals.com/files/Handle.zip

# Define the URLs for the files to be downloaded
$ssdeepURL = "https://github.com/ssdeep-project/ssdeep/releases/download/release-2.14.1/ssdeep-2.14.1-win32-binary.zip"
$handleURL = "https://download.sysinternals.com/files/Handle.zip"

# Define the target directories
$ssdeepDir = "xcyclopedia\script\bin"
$handleDir = "xcyclopedia\script\bin\sysinternals\handle"

# Define the expected executable paths
$ssdeepExe = Join-Path $ssdeepDir "ssdeep.exe"
$handleExe = Join-Path $handleDir "handle.exe"

# Check if ssdeep.exe exists
if (-not (Test-Path -Path $ssdeepExe)) {
    # Create the ssdeep directory if it doesn't exist
    if (-not (Test-Path -Path $ssdeepDir)) {
        New-Item -ItemType Directory -Path $ssdeepDir -Force
    }
    # Download ssdeep
    Invoke-WebRequest -Uri $ssdeepURL -OutFile "$ssdeepDir\ssdeep-2.14.1-win32-binary.zip"
    # Unzip ssdeep
    Expand-Archive -LiteralPath "$ssdeepDir\ssdeep-2.14.1-win32-binary.zip" -DestinationPath $ssdeepDir -Force
    # Clean up the ZIP file
    Remove-Item "$ssdeepDir\ssdeep-2.14.1-win32-binary.zip"
}

# Check if handle.exe exists
if (-not (Test-Path -Path $handleExe)) {
    # Create the handle directory if it doesn't exist
    if (-not (Test-Path -Path $handleDir)) {
        New-Item -ItemType Directory -Path $handleDir -Force
    }
    # Download Handle
    Invoke-WebRequest -Uri $handleURL -OutFile "$handleDir\Handle.zip"
    # Unzip Handle
    Expand-Archive -LiteralPath "$handleDir\Handle.zip" -DestinationPath $handleDir -Force
    # Clean up the ZIP file
    Remove-Item "$handleDir\Handle.zip"
}


# .\xcyclopedia\script\Get-Xcyclopedia.ps1 -save_path ".\output" -take_screenshots -minimize_windows -target_file_extension ".exe,.lnk" -execute_files -target_path_recursive "$env:APPDATA\Microsoft\Windows\Start Menu\Programs,$env:ProgramFiles\,${env:ProgramFiles(x86)}\,$env:windir\system32"
.\xcyclopedia\script\Get-Xcyclopedia.ps1 -save_path "$env:USERPROFILE\source\repos\OSVisualInstruct\output" -take_screenshots -minimize_windows -target_file_extension ".exe",".lnk" -execute_files -target_path_recursive "$env:APPDATA\Microsoft\Windows\Start Menu\Programs","$env:ProgramFiles","${env:ProgramFiles(x86)}","$env:LOCALAPPDATA"
