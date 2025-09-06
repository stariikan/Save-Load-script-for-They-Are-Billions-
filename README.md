This script allows you to quickly backup and restore (Save/Load) your “They Are Billions” game folder (user's saves) using simple hotkeys on Windows. It works in the background, shows notifications, and keeps a log of actions.

Main Features:
- Flexible paths for any user
- Automatically detects the current Windows user.


Uses the standard Documents folder:
- C:\Users\CurrentUser\Documents\My Games\They Are Billions

Backups are stored in:
- C:\Users\CurrentUser\Backups_TAB

Log file on Desktop:
- C:\Users\CurrentUser\Desktop\tab_backup_log.txt


Hotkey Control
- F5 → Creates a backup of the current folder with a timestamp.
- F9 → Restores the latest backup, replacing the current folder.
- F11 → Exits the script.

Background Operation
- Runs silently using pythonw.exe or as a .pyw file.
- No console window pops up.

Notifications
- Uses Windows toast notifications to show success or error messages.
- Logs all actions with timestamps in a text file on Desktop.

Backup Management:
- Each backup folder is timestamped (Backup_YYYY-MM-DD_HH-MM-SS).
- Restore always uses the most recent backup automatically.

Requirements:
- Python
- Python libraries: keyboard, win10toast.
Optional: run as .pyw or with pythonw.exe for fully hidden background operation.

How It Works (Step by Step)
- Install Python (if not already installed).
- Install the required libraries.
- Once Python works in CMD run: - pip install keyboard win10toast
- Copy the script and the .bat file to: C:\Users\CurrentUser\
- In start_backup.bat, replace "CurrentUser" with your actual Windows username.
- Run start_backup.bat.
- When the game saves and you want to back it up, press F5.
- To restore the most recent backup, press F9 in the main menu.
- Then load the profile you were playing.

Waits for hotkeys:
- Press F5 → copies the game folder to the backup folder with a timestamp.
- Press F9 → deletes current folder and restores from the latest backup.
- Press F11 → stops the script.

Each action logs a message to the Desktop log file and shows a Windows notification.
