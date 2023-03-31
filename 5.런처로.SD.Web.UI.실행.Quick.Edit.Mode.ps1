$RootDir = (Get-Location).Path
$VenvDir = (Join-Path $RootDir "venv")
$TempDir = (Join-Path $RootDir "temp")
$Python = "python"
$Git = "git"

# Script commands to disable quick edit mode
# - https://stackoverflow.com/a/42792718
$QuickEditCodeSnippet = @" 
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Runtime.InteropServices;

 
public static class DisableConsoleQuickEdit
{
 
const uint ENABLE_QUICK_EDIT = 0x0040;

// STD_INPUT_HANDLE (DWORD): -10 is the standard input device.
const int STD_INPUT_HANDLE = -10;

[DllImport("kernel32.dll", SetLastError = true)]
static extern IntPtr GetStdHandle(int nStdHandle);

[DllImport("kernel32.dll")]
static extern bool GetConsoleMode(IntPtr hConsoleHandle, out uint lpMode);

[DllImport("kernel32.dll")]
static extern bool SetConsoleMode(IntPtr hConsoleHandle, uint dwMode);

public static bool SetQuickEdit(bool SetEnabled)
{

    IntPtr consoleHandle = GetStdHandle(STD_INPUT_HANDLE);

    // get current console mode
    uint consoleMode;
    if (!GetConsoleMode(consoleHandle, out consoleMode))
    {
        // ERROR: Unable to get console mode.
        return false;
    }

    // Clear the quick edit bit in the mode flags
    if (SetEnabled)
    {
        consoleMode &= ~ENABLE_QUICK_EDIT;
    }
    else
    {
        consoleMode |= ENABLE_QUICK_EDIT;
    }

    // set the new mode
    if (!SetConsoleMode(consoleHandle, consoleMode))
    {
        // ERROR: Unable to set console mode
        return false;
    }

    return true;
}
}
"@

$QuickEditMode = add-type -TypeDefinition $QuickEditCodeSnippet -Language CSharp


function Set-QuickEdit() {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $false, HelpMessage = "This switch will disable Console QuickEdit option")]
        [switch]$DisableQuickEdit = $false
    )


    if ([DisableConsoleQuickEdit]::SetQuickEdit($DisableQuickEdit)) {
        Write-Output "QuickEdit settings has been updated."
    }
    else {
        Write-Output "Something went wrong."
    }
}

Set-QuickEdit -DisableQuickEdit

$Deactivate = @(
    { Remove-Item -Recurse -Force "${TempDir}" }
)

Start-Transcript -Path  (Join-Path "log" "launcher.log")
try {
    try {
        try {
            Write-Output "Startup: (1/5) 설치된 Python 버전을 확인합니다."
            $PythonCommand = (Get-Command $Python -ErrorAction SilentlyContinue)
            if ($PythonCommand.Version.Major -lt 3) {
                throw "설치된 Python 버전이 $($PythonCommand.Version)로 낮습니다."
            }
            if ($PythonCommand.Version.Minor -lt 10) {
                throw "설치된 Python 버전이 $($PythonCommand.Version)로 낮습니다."
            }
            if ($PythonCommand.Version.Build -lt 6000) {
                throw "설치된 Python 버전이 $($PythonCommand.Version)로 낮습니다."
            }
        }
        catch [System.Management.Automation.CommandNotFoundException] {
            throw "설치된 Python을 찾을 수 없습니다."
        }
    }
    catch {
        # https://www.python.org/downloads/windows/
        $DownloadUrl = if ([Environment]::Is64BitOperatingSystem)
        { "https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe" } else 
        { "https://www.python.org/ftp/python/3.10.9/python-3.10.9.exe" }

        throw "$_ 다음 링크를 통해 Python을 설치해 주세요. ${DownloadUrl}"
    }

    try {
        try {
            Write-Output "Startup: (2/5) 설치된 Git 버전을 확인합니다."
            $GitCommand = (Get-Command $Git -ErrorAction SilentlyContinue)
            if ($GitCommand.Version.Major -lt 2) {
                throw "설치된 Git 버전이 $($GitCommand.Version)로 낮습니다."
            }
            if ($GitCommand.Version.Minor -lt 32) {
                throw "설치된 Git 버전이 $($GitCommand.Version)로 낮습니다."
            }
        }
        catch [System.Management.Automation.CommandNotFoundException] {
            throw "설치된 Git 찾을 수 없습니다."
        }
    }
    catch {
        # https://github.com/git-for-windows/git/releases
        $DownloadUrl = if ([Environment]::Is64BitOperatingSystem)
        { "https://github.com/git-for-windows/git/releases/download/v2.40.0.windows.1/Git-2.40.0-64-bit.exe" } else 
        { "https://github.com/git-for-windows/git/releases/download/v2.40.0.windows.1/Git-2.40.0-32-bit.exe" }

        throw "$_ 다음 링크를 통해 Git 설치해 주세요. ${DownloadUrl} 설치 옵션으로 Use Git from the Windows Command Prompt을 선택해 주세요."
    }

    Write-Output "Startup: (3/5) pip 모듈을 확인합니다."
    & $Python -m pip --help | Out-Null
    if ($LASTEXITCODE -ne 0) {
        $GetPipPath = (Join-Path $TempDir "get-pip.py")
        Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile "${GetPipPath}"

        & $Python GetPipPath
        if ($LASTEXITCODE -ne 0) {
            throw "pip 모듈을 설치 할 수 없습니다."
        }
    }

    Write-Output "Startup: (4/5) 가상 환경을 ${VenvDir} 디렉터리에 구성합니다."
    & $Python -m venv ${VenvDir}
    if ($LASTEXITCODE -ne 0) {
        throw "가상 환경을 ${VenvDir} 디렉터리에 구성할 수 없습니다."
    }
 
    Write-Output "Startup: (5/5) 런처를 시작합니다."
    $Activate = (Join-Path $VenvDir -ChildPath "Scripts" | Join-Path -ChildPath "Activate.ps1")
    $Deactivate += { deactivate }
    $Python = (Join-Path $VenvDir -ChildPath "Scripts" | Join-Path -ChildPath $Python)
    & ${Activate} -VenvDir ${VenvDir}; & $Python app.py --inbrowser;
    if ($LASTEXITCODE -ne 0) {
        throw "런처가 비정상 종료되었습니다."
    }
}
catch {
    Write-Warning "$_"
}
finally {
    $Deactivate | ForEach-Object { $_.Invoke() }
    Stop-Transcript
    Read-Host -Prompt "작업을 종료하려면 아무키나 누르세요"
}
