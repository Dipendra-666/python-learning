import shutil
import datetime

source_folder = "project"

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

backup_folder = f"backup_{timestamp}"

shutil.copytree(source_folder, backup_folder)

print(f"Backup created: {backup_folder}")