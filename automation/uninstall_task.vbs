' uninstall_task.vbs
' Self-elevating uninstaller that removes the scheduled task

Option Explicit

Dim shell, taskName, params
Set shell = CreateObject("WScript.Shell")

taskName = "DownloadsFolderOrganizer"

' Relaunch as Administrator if not already elevated
If Not WScript.Arguments.Named.Exists("elevated") Then
    params = """" & WScript.ScriptFullName & """ /elevated"
    shell.Run "powershell -Command Start-Process wscript -Verb runAs -ArgumentList '" & params & "'", 0, True
    WScript.Quit
End If

' Delete the scheduled task silently
shell.Run "schtasks /delete /tn """ & taskName & """ /f", 0, True

' Confirm successful removal
MsgBox "Downloads Folder Organizer has been successfully uninstalled." & vbCrLf & vbCrLf & _
       "The background task has been removed and it will no longer run automatically.", _
       vbInformation, "Uninstallation Complete"
