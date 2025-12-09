import os
import shutil

class FileInterface:
    def __init__(self):
        pass

    def create_file(self, path, content):
        """Create a file with given content."""
        try:
            with open(path, 'w') as f:
                f.write(content)
            return f"File {path} created successfully.", "", 0
        except Exception as e:
            return "", str(e), 1

    def read_file(self, path):
        """Read the content of a file."""
        try:
            with open(path, 'r') as f:
                content = f.read()
            return content, "", 0
        except Exception as e:
            return "", str(e), 1

    def delete_file(self, path):
        """Delete a file."""
        try:
            os.remove(path)
            return f"File {path} deleted successfully.", "", 0
        except Exception as e:
            return "", str(e), 1

    def list_directory(self, path):
        """List contents of a directory."""
        try:
            contents = os.listdir(path)
            return "\n".join(contents), "", 0
        except Exception as e:
            return "", str(e), 1

    def move_file(self, src, dst):
        """Move or rename a file."""
        try:
            shutil.move(src, dst)
            return f"File moved from {src} to {dst}.", "", 0
        except Exception as e:
            return "", str(e), 1