import requests

class NetworkInterface:
    def __init__(self):
        pass

    def download_file(self, url, dest_path):
        """Download a file from URL to destination path."""
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(dest_path, 'wb') as f:
                f.write(response.content)
            return f"File downloaded to {dest_path}.", "", 0
        except Exception as e:
            return "", str(e), 1

    def get_web_content(self, url):
        """Fetch content from a URL."""
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text, "", 0
        except Exception as e:
            return "", str(e), 1

    def post_data(self, url, data):
        """Post data to a URL."""
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.text, "", 0
        except Exception as e:
            return "", str(e), 1