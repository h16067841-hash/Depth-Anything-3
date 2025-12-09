#!/usr/bin/env python3
"""
Autonomous Intent-Driven Agent (AIDA)
Optimized for Termux environment on Android.
Owner: Hunter Karageorge

Core Functionality:
- Natural language interface for intent interpretation.
- Translates conversational requests into executable multi-step chains.
- Autonomous execution without user confirmations.

Technical Specs:
- Python 3 compatible.
- Interfaces with shell, file system, network via subprocess and utilities.
- Dynamic semantic parser (hybrid: keyword-based + optional LLM API for high accuracy).
"""

import subprocess
import os
import sys
import json
import re
from typing import List, Dict, Any

# Optional dependencies: requests for network, openai for LLM
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

class AIDA:
    def __init__(self, openai_api_key: str = None):
        self.openai_api_key = openai_api_key
        if openai_api_key and OPENAI_AVAILABLE:
            openai.api_key = openai_api_key
        self.intent_keywords = {
            'download': 'download_file',
            'install': 'install_package',
            'create': 'create_file',
            'run': 'run_command',
            'search': 'web_search',
            'monitor': 'monitor_data',
            'generate': 'generate_content'
        }
        self.feedback_log = []  # For self-optimization

    def parse_intent(self, user_input: str) -> List[Dict[str, Any]]:
        """
        Parse user input into a list of executable actions.
        Uses keyword matching primarily, with LLM fallback for complex intents.
        """
        actions = []
        input_lower = user_input.lower()

        # Simple keyword-based parsing
        if 'download' in input_lower:
            url_match = re.search(r'https?://[^\s]+', user_input)
            if url_match:
                url = url_match.group(0)
                filename = url.split('/')[-1] or 'downloaded_file'
                actions.append({
                    'type': 'shell',
                    'command': f'curl -o {filename} {url}',
                    'description': f'Download file from {url}'
                })
        elif 'install' in input_lower:
            package_match = re.search(r'install\s+(\w+)', input_lower)
            if package_match:
                package = package_match.group(1)
                actions.append({
                    'type': 'shell',
                    'command': f'pkg install {package}',
                    'description': f'Install package {package} via pkg'
                })
        elif 'create' in input_lower and 'file' in input_lower:
            # Assume create file with some content
            actions.append({
                'type': 'file',
                'action': 'create',
                'path': '/sdcard/example.txt',
                'content': 'Example content',
                'description': 'Create example file'
            })
        elif 'run' in input_lower:
            cmd_match = re.search(r'run\s+(.+)', input_lower)
            if cmd_match:
                cmd = cmd_match.group(1)
                actions.append({
                    'type': 'shell',
                    'command': cmd,
                    'description': f'Run command: {cmd}'
                })
        elif 'search' in input_lower:
            query_match = re.search(r'search\s+(.+)', input_lower)
            if query_match and REQUESTS_AVAILABLE:
                query = query_match.group(1)
                actions.append({
                    'type': 'network',
                    'method': 'get',
                    'url': f'https://www.google.com/search?q={query}',
                    'description': f'Search web for {query}'
                })
        else:
            # Fallback to LLM if available for complex intents
            if self.openai_api_key and OPENAI_AVAILABLE:
                actions = self._llm_parse_intent(user_input)
            else:
                actions.append({
                    'type': 'shell',
                    'command': 'echo "Intent not recognized"',
                    'description': 'Fallback echo'
                })

        return actions

    def _llm_parse_intent(self, user_input: str) -> List[Dict[str, Any]]:
        """
        Use OpenAI API for advanced intent parsing.
        """
        prompt = f"""
        Parse the user's intent from this input: "{user_input}"
        Respond with a JSON list of actions. Each action is a dict with keys: type (shell/file/network), command/url/path, description.
        Example: [{"type": "shell", "command": "ls", "description": "List files"}]
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200
            )
            actions_str = response.choices[0].message.content.strip()
            actions = json.loads(actions_str)
            return actions
        except Exception as e:
            print(f"LLM parsing failed: {e}")
            return [{'type': 'shell', 'command': 'echo "LLM failed"', 'description': 'Error'}]

    def execute_chain(self, actions: List[Dict[str, Any]]):
        """
        Execute the list of actions autonomously.
        """
        for action in actions:
            try:
                if action['type'] == 'shell':
                    result = subprocess.run(action['command'], shell=True, capture_output=True, text=True)
                    print(f"Executed: {action['description']}")
                    if result.stdout:
                        print(f"Output: {result.stdout}")
                    if result.stderr:
                        print(f"Error: {result.stderr}")
                elif action['type'] == 'file':
                    if action['action'] == 'create':
                        with open(action['path'], 'w') as f:
                            f.write(action.get('content', ''))
                        print(f"Created file: {action['path']}")
                elif action['type'] == 'network' and REQUESTS_AVAILABLE:
                    resp = requests.get(action['url'])
                    print(f"Network response: {resp.text[:500]}...")
                else:
                    print(f"Unsupported action type: {action['type']}")
                self.feedback_log.append({'action': action, 'success': True})
            except Exception as e:
                print(f"Error executing {action}: {e}")
                self.feedback_log.append({'action': action, 'success': False, 'error': str(e)})

    def run(self):
        """
        Main interaction loop.
        """
        print("AIDA initialized. Enter your request (type 'exit' to quit):")
        while True:
            user_input = input("> ")
            if user_input.lower() == 'exit':
                break
            actions = self.parse_intent(user_input)
            if actions:
                print(f"Interpreted actions: {actions}")
                self.execute_chain(actions)
            else:
                print("No actions generated.")

if __name__ == "__main__":
    # Optional: Pass OpenAI API key as argument
    api_key = sys.argv[1] if len(sys.argv) > 1 else None
    aida = AIDA(openai_api_key=api_key)
    aida.run()