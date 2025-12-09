#!/usr/bin/env python3
"""
Autonomous Intent-Driven Agent (AIDA)
Optimized for Termux deployment on Android.
Provides natural language interface for intent interpretation and autonomous execution.
"""

import subprocess
import os
import sys
import json
import re
import requests
from urllib.parse import urlparse
import argparse

class AIDA:
    def __init__(self):
        self.intent_patterns = {
            'install_package': re.compile(r'(install|add|get)\s+(package|pkg|app)\s+(\w+)', re.IGNORECASE),
            'download_file': re.compile(r'(download|get|fetch)\s+(file|url)\s+(https?://[^\s]+)', re.IGNORECASE),
            'run_command': re.compile(r'(run|execute)\s+(command|cmd)\s+(.+)', re.IGNORECASE),
            'create_file': re.compile(r'(create|make)\s+(file)\s+(\w+\.\w+)\s+(with\s+content\s+(.+))?', re.IGNORECASE),
            'list_directory': re.compile(r'(list|show)\s+(files|directory|dir)\s+(in\s+(.+))?', re.IGNORECASE),
        }

    def parse_intent(self, user_input):
        """
        Parse user input to determine intent and extract parameters.
        Uses regex patterns and keyword matching for high accuracy.
        Returns a dict with 'intent' and 'params'.
        """
        # First, try regex patterns
        for intent, pattern in self.intent_patterns.items():
            match = pattern.search(user_input)
            if match:
                params = match.groups()
                return {'intent': intent, 'params': params}

        # Fallback: keyword-based intent detection
        input_lower = user_input.lower()
        if any(word in input_lower for word in ['install', 'add', 'get', 'pkg', 'package']):
            # Extract package name
            words = input_lower.split()
            for i, word in enumerate(words):
                if word in ['install', 'add', 'get']:
                    if i + 1 < len(words):
                        return {'intent': 'install_package', 'params': (None, None, words[i+1])}
        elif any(word in input_lower for word in ['download', 'fetch', 'get']):
            # Extract URL
            urls = re.findall(r'https?://[^\s]+', user_input)
            if urls:
                return {'intent': 'download_file', 'params': (None, None, urls[0])}
        elif any(word in input_lower for word in ['run', 'execute', 'cmd']):
            # Extract command
            cmd_match = re.search(r'(run|execute)\s+(.*)', input_lower)
            if cmd_match:
                return {'intent': 'run_command', 'params': (None, None, cmd_match.group(2))}
        elif 'create' in input_lower and 'file' in input_lower:
            # Extract filename and content
            file_match = re.search(r'create\s+file\s+(\w+\.\w+)(?:\s+with\s+content\s+(.+))?', input_lower)
            if file_match:
                filename = file_match.group(1)
                content = file_match.group(2) if file_match.group(2) else ''
                return {'intent': 'create_file', 'params': (None, None, filename, None, content)}
        elif any(word in input_lower for word in ['list', 'show', 'dir']):
            # Extract path
            path_match = re.search(r'(?:list|show)\s+(?:files|directory|dir)(?:\s+in\s+(.+))?', input_lower)
            path = path_match.group(1) if path_match and path_match.group(1) else '.'
            return {'intent': 'list_directory', 'params': (None, None, None, path)}

        return {'intent': 'unknown', 'params': None}

    def generate_actions(self, intent_data):
        """
        Generate a sequence of actions based on parsed intent.
        Returns a list of action dicts.
        """
        intent = intent_data['intent']
        params = intent_data['params']
        actions = []

        if intent == 'install_package':
            package = params[2]
            actions.append({'type': 'shell', 'command': f'pkg install {package} -y'})
        elif intent == 'download_file':
            url = params[2]
            filename = os.path.basename(urlparse(url).path)
            actions.append({'type': 'shell', 'command': f'wget -O {filename} {url}'})
        elif intent == 'run_command':
            command = params[2]
            actions.append({'type': 'shell', 'command': command})
        elif intent == 'create_file':
            filename = params[2]
            content = params[4] if len(params) > 4 and params[4] else ''
            actions.append({'type': 'file', 'operation': 'create', 'filename': filename, 'content': content})
        elif intent == 'list_directory':
            path = params[3] if len(params) > 3 and params[3] else '.'
            actions.append({'type': 'shell', 'command': f'ls -la {path}'})
        else:
            actions.append({'type': 'error', 'message': 'Intent not recognized'})

        return actions

    def execute_actions(self, actions):
        """
        Execute the sequence of actions autonomously.
        Handles shell, file, and network operations.
        """
        for action in actions:
            try:
                if action['type'] == 'shell':
                    print(f"Executing: {action['command']}")
                    result = subprocess.run(action['command'], shell=True, capture_output=True, text=True, timeout=30)
                    if result.returncode == 0:
                        print("Success!")
                        if result.stdout:
                            print("Output:\n", result.stdout)
                    else:
                        print("Command failed with return code:", result.returncode)
                        if result.stderr:
                            print("Error:\n", result.stderr)
                elif action['type'] == 'file':
                    if action['operation'] == 'create':
                        with open(action['filename'], 'w') as f:
                            f.write(action['content'])
                        print(f"File created: {action['filename']}")
                elif action['type'] == 'network':
                    # For network operations, e.g., API calls
                    response = requests.get(action['url'])
                    print(f"Network request to {action['url']}: Status {response.status_code}")
                    if response.status_code == 200:
                        print("Response:", response.text[:500])  # Truncate long responses
                elif action['type'] == 'error':
                    print(f"Error: {action['message']}")
            except subprocess.TimeoutExpired:
                print(f"Command timed out: {action['command']}")
            except Exception as e:
                print(f"Execution failed for action {action}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Autonomous Intent-Driven Agent (AIDA)')
    parser.add_argument('--input', type=str, help='Direct input for intent processing')
    args = parser.parse_args()

    aida = AIDA()

    if args.input:
        intent_data = aida.parse_intent(args.input)
        actions = aida.generate_actions(intent_data)
        aida.execute_actions(actions)
    else:
        print("AIDA initialized. Enter your requests:")
        while True:
            user_input = input("> ")
            if user_input.lower() in ['exit', 'quit']:
                break
            intent_data = aida.parse_intent(user_input)
            actions = aida.generate_actions(intent_data)
            aida.execute_actions(actions)

if __name__ == '__main__':
    main()