import os

def check_for_app_folder():
    apps_folder = os.path.expanduser("~/.apps")
    os.makedirs(apps_folder, exist_ok=True)