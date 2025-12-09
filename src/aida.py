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
        Returns a dict with 'intent' and 'params'.
        """
        for intent, pattern in self.intent_patterns.items():
            match = pattern.search(user_input)
            if match:
                params = match.groups()
                return {'intent': intent, 'params': params}
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
        """
        for action in actions:
            try:
                if action['type'] == 'shell':
                    result = subprocess.run(action['command'], shell=True, capture_output=True, text=True)
                    print(f"Executed: {action['command']}")
                    if result.stdout:
                        print("Output:", result.stdout)
                    if result.stderr:
                        print("Error:", result.stderr)
                elif action['type'] == 'file':
                    if action['operation'] == 'create':
                        with open(action['filename'], 'w') as f:
                            f.write(action['content'])
                        print(f"Created file: {action['filename']}")
                elif action['type'] == 'error':
                    print(f"Error: {action['message']}")
            except Exception as e:
                print(f"Execution failed: {e}")

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