#!/usr/bin/env python3

import re
from shell_interface import ShellInterface
from file_interface import FileInterface
from network_interface import NetworkInterface

class IntentParser:
    def __init__(self):
        self.shell = ShellInterface()
        self.file = FileInterface()
        self.network = NetworkInterface()

    def parse_intent(self, user_input):
        """Parse user input to determine intent and extract parameters."""
        actions = []

        # Download file intent
        if re.search(r'download\s+(https?://[^\s]+)', user_input, re.IGNORECASE):
            url = re.search(r'download\s+(https?://[^\s]+)', user_input, re.IGNORECASE).group(1)
            dest = re.search(r'to\s+([^\s]+)', user_input, re.IGNORECASE)
            dest_path = dest.group(1) if dest else 'downloaded_file'
            actions.append(('download', url, dest_path))

        # Run command intent
        elif re.search(r'run\s+(.+)', user_input, re.IGNORECASE):
            command = re.search(r'run\s+(.+)', user_input, re.IGNORECASE).group(1)
            actions.append(('run_command', command))

        # Create file intent
        elif re.search(r'create\s+(?:a\s+)?file\s+(?:named\s+)?([^\s]+)\s+with\s+content\s+(.+)', user_input, re.IGNORECASE):
            match = re.search(r'create\s+(?:a\s+)?file\s+(?:named\s+)?([^\s]+)\s+with\s+content\s+(.+)', user_input, re.IGNORECASE)
            path = match.group(1)
            content = match.group(2)
            actions.append(('create_file', path, content))

        # Read file intent
        elif re.search(r'read\s+(?:file\s+)?([^\s]+)', user_input, re.IGNORECASE):
            path = re.search(r'read\s+(?:file\s+)?([^\s]+)', user_input, re.IGNORECASE).group(1)
            actions.append(('read_file', path))

        # List directory intent
        elif re.search(r'list\s+(?:directory\s+)?([^\s]+)', user_input, re.IGNORECASE):
            path = re.search(r'list\s+(?:directory\s+)?([^\s]+)', user_input, re.IGNORECASE).group(1)
            actions.append(('list_dir', path))

        # Get web content intent
        elif re.search(r'get\s+(?:content\s+from\s+)?(?:web\s+)?(?:page\s+)?(?:at\s+)?(https?://[^\s]+)', user_input, re.IGNORECASE):
            url = re.search(r'get\s+(?:content\s+from\s+)?(?:web\s+)?(?:page\s+)?(?:at\s+)?(https?://[^\s]+)', user_input, re.IGNORECASE).group(1)
            actions.append(('get_web', url))

        # Default to shell command if no specific intent
        else:
            actions.append(('run_command', user_input))

        return actions

    def execute_actions(self, actions):
        """Execute the parsed actions."""
        results = []
        for action in actions:
            if action[0] == 'download':
                stdout, stderr, code = self.network.download_file(action[1], action[2])
                results.append((stdout, stderr, code))
            elif action[0] == 'run_command':
                stdout, stderr, code = self.shell.execute_command(action[1])
                results.append((stdout, stderr, code))
            elif action[0] == 'create_file':
                stdout, stderr, code = self.file.create_file(action[1], action[2])
                results.append((stdout, stderr, code))
            elif action[0] == 'read_file':
                stdout, stderr, code = self.file.read_file(action[1])
                results.append((stdout, stderr, code))
            elif action[0] == 'list_dir':
                stdout, stderr, code = self.file.list_directory(action[1])
                results.append((stdout, stderr, code))
            elif action[0] == 'get_web':
                stdout, stderr, code = self.network.get_web_content(action[1])
                results.append((stdout, stderr, code))
        return results

def main():
    parser = IntentParser()
    print("AIDA: Autonomous Intent-Driven Agent initialized.")
    print("Enter your request (type 'exit' to quit):")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            break
        actions = parser.parse_intent(user_input)
        results = parser.execute_actions(actions)
        for stdout, stderr, code in results:
            if stdout:
                print(stdout)
            if stderr:
                print(f"Error: {stderr}")
            if code != 0:
                print(f"Exit code: {code}")

if __name__ == "__main__":
    main()