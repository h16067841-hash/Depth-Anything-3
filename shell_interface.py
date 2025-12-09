import subprocess
import os

class ShellInterface:
    def __init__(self):
        pass

    def execute_command(self, command):
        """Execute a shell command and return the output."""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=os.getcwd())
            return result.stdout, result.stderr, result.returncode
        except Exception as e:
            return "", str(e), 1

    def run_background_command(self, command):
        """Run a command in the background."""
        try:
            subprocess.Popen(command, shell=True, cwd=os.getcwd())
            return "Command started in background.", "", 0
        except Exception as e:
            return "", str(e), 1