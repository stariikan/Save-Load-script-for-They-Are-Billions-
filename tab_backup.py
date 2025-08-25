import os
import shutil
import datetime
import keyboard
from win10toast import ToastNotifier
import re
from datetime import datetime as dt

# === CONFIG ===
user_home = os.path.expanduser("~")

# Paths
source = os.path.join(user_home, r"Documents\My Games\They Are Billions")
backup_dir = os.path.join(user_home, r"Backups_TAB")
log_file = os.path.join(user_home, "Desktop", "tab_backup_log.txt")

# Create backup folder if missing
os.makedirs(backup_dir, exist_ok=True)

# Init Windows notifier
toaster = ToastNotifier()

# Logging + notification function
def notify(msg, title="They Are Billions Backup"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {msg}\n")
    toaster.show_toast(title, msg, duration=4, threaded=True)

# Backup function
def backup():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dest = os.path.join(backup_dir, f"Backup_{timestamp}")
    try:
        shutil.copytree(source, dest)
        notify(f"Backup created: {dest}")
    except Exception as e:
        notify(f"Backup failed: {e}", "ERROR")

# Restore function (most recent backup based on timestamp in folder name)
def restore():
    try:
        backups = [d for d in os.listdir(backup_dir) if os.path.isdir(os.path.join(backup_dir, d))]
        if not backups:
            notify("No backups found!", "ERROR")
            return

        # Extract timestamp from folder name
        backup_times = []
        for b in backups:
            match = re.search(r'Backup_(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})', b)
            if match:
                backup_dt = dt.strptime(match.group(1), "%Y-%m-%d_%H-%M-%S")
                backup_times.append((backup_dt, b))

        if not backup_times:
            notify("No valid backups found!", "ERROR")
            return

        # Pick the latest backup by timestamp
        latest_backup_name = max(backup_times, key=lambda x: x[0])[1]
        latest_backup_path = os.path.join(backup_dir, latest_backup_name)

        # Remove current folder if it exists
        if os.path.exists(source):
            shutil.rmtree(source)

        # Restore the latest backup
        shutil.copytree(latest_backup_path, source)
        notify(f"Folder replaced with latest backup: {latest_backup_path}")

    except Exception as e:
        notify(f"Restore failed: {e}", "ERROR")

# Exit function
def exit_program():
    notify("Backup program exited.")
    os._exit(0)

# Hotkeys
keyboard.add_hotkey("F5", backup)
keyboard.add_hotkey("F9", restore)
keyboard.add_hotkey("F11", exit_program)

notify("Backup program started. (F5=backup, F9=restore, F11=exit)")

# Keep script running in background
keyboard.wait()
