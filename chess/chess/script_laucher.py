import subprocess
import os
import sys

script_path = os.path.abspath("chess/chess/frontend.py")

startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

# Run the script in the background without opening a terminal window
subprocess.Popen([sys.executable, script_path], startupinfo=startupinfo, close_fds=True)