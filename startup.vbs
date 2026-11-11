Option Explicit

Dim shell, fso
Dim pythonPath, scriptPath, projectFolder
Dim command

Set shell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' CHANGE THIS PATH to pythonw.exe instead of python.exe
pythonPath = "C:\Users\harsh\AppData\Local\Programs\Python\Python313\pythonw.exe"

' Existing project location
projectFolder = "C:\Users\harsh\OneDrive\Desktop\Dushant\Cyber-Projects\LaptopWebcam"
scriptPath = projectFolder & "\main.py"

If Not fso.FileExists(pythonPath) Then
    MsgBox "Python executable not found! Check pythonw.exe path.", vbCritical
    WScript.Quit
End If

If Not fso.FileExists(scriptPath) Then
    MsgBox "main.py not found!", vbCritical
    WScript.Quit
End If

' Set working directory for config/.env
shell.CurrentDirectory = projectFolder

' Launch application completely hidden (0 = hidden, False = don't wait)
command = """" & pythonPath & """ """ & scriptPath & """"
shell.Run command, 0, False

Set fso = Nothing
Set shell = Nothing