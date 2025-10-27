' install_task.vbs
' Installs the Downloads Folder Organizer to run once now and on every user login

Option Explicit

Dim shell, fs, taskName, batPath, cmd, params
Set shell = CreateObject("WScript.Shell")
Set fs = CreateObject("Scripting.FileSystemObject")

taskName = "DownloadsFolderOrganizer"

' Relaunch as Administrator if not already elevated
If Not WScript.Arguments.Named.Exists("elevated") Then
    params = """" & WScript.ScriptFullName & """ /elevated"
    shell.Run "powershell -Command Start-Process wscript -Verb runAs -ArgumentList '" & params & "'", 0, True
    WScript.Quit
End If

' Build absolute path to the batch file
batPath = fs.GetParentFolderName(WScript.ScriptFullName) & "\run_organizer.bat"

' Create the scheduled task (runs at every user login, with highest privileges)
cmd = "schtasks /create /tn """ & taskName & """ /tr """ & batPath & _
      """ /sc onlogon /f /rl highest"

' Run the command silently
shell.Run cmd, 0, True

' Run the organizer immediately once after installation
shell.Run """" & batPath & """", 0, False

' Display success message
MsgBox "Downloads Folder Organizer has been successfully installed!" & vbCrLf & vbCrLf & _
       "- Runs immediately after installation" & vbCrLf & _
       "- Automatically runs every time you log in" & vbCrLf & _
       "No further action is required.", _
       vbInformation, "Installation Complete"
