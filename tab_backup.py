import os
import shutil
import datetime
import keyboard
from win10toast import ToastNotifier

# === CONFIG ===
# Get current user's home directory (e.g. C:\Users\John)
user_home = os.path.expanduser("~")

# Paths based on current user
source = os.path.join(user_home, r"Documents\My Games\They Are Billions")
backup_dir = os.path.join(user_home, r"Backups_TAB")
log_file = os.path.join(user_home, "Desktop", "tab_backup_log.txt")

# Create backup folder if missing
os.makedirs(backup_dir, exist_ok=True)

# Init notifier
toaster = ToastNotifier()

# Logging + notification
def notify(msg, title="They Are Billions Backup"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {msg}\n")
    toaster.show_toast(title, msg, duration=4, threaded=True)

def backup():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dest = os.path.join(backup_dir, f"Backup_{timestamp}")
    try:
        shutil.copytree(source, dest)
        notify(f"Backup created: {dest}")
    except Exception as e:
        notify(f"Backup failed: {e}", "ERROR")

def restore():
    try:
        backups = [os.path.join(backup_dir, d) for d in os.listdir(backup_dir)]
        backups = [d for d in backups if os.path.isdir(d)]
        if not backups:
            notify("No backups found!", "ERROR")
            return
        
        latest = max(backups, key=os.path.getmtime)

        # Remove current folder
        if os.path.exists(source):
            shutil.rmtree(source)

        # Restore from latest
        shutil.copytree(latest, source)
        notify(f"Folder replaced with latest backup: {latest}")  # ✅ Notification added
    except Exception as e:
        notify(f"Restore failed: {e}", "ERROR")

# Hotkeys
keyboard.add_hotkey("F5", backup)
keyboard.add_hotkey("F9", restore)

notify("Backup program started. (F5=backup, F9=restore, F11=exit)")

# Wait for F11 to exit
keyboard.wait("F11")
notify("Backup program exited.")  # ✅ Notification when exiting
