
"""
Howdy partner! We're about to embark on a fun journey called "Maintain clipboard history accessible via CLI." 
Strap in, and let's get going!

Oh, and also, just a friendly reminder: No GUIs, APIs, or Internet access. Just good ol' Python - KISS (Keep It Simple, Silly) at its best.
"""

import os
import sys
import tempfile
from pathlib import Path

# We are using the built-in modules os, sys, pathlib, and tempfile, so no worries about dependencies or portability!


class ClipboardHistory:
    """
    Yeehaw! Here's our ClipboardHistory class, the heart of our project.

    It manages saving and loading your clipboard history.
    """

    # Let's define the file where we're going to store our clipboard history.
    # We'll use Python's built-in tempfile module to ensure it works on any OS.
    FILE_NAME = Path(tempfile.gettempdir()) / "clipboard_history.txt"

    def __init__(self):
        """
        Initialize the "clipboard_history" attribute as an empty list. This'll store our clipboard data.
        """
        self.clipboard_history = []

    def load_history(self):
        """
        This method is our trusty loader, used to open and read our history file.

        If the file doesn't exist, we won't sweat it - we'll just start with an empty history.
        """
        if self.FILE_NAME.exists():
            with open(self.FILE_NAME, "r") as file:
                self.clipboard_history = file.readlines()

    def save_history(self):
        """
        This companion to our loader writes our clipboard history to our history file every time there's a change.

        A write for every change keeps our history always up-to-date.
        """
        with open(self.FILE_NAME, "w") as file:
            file.writelines(self.clipboard_history)

    def add_clipboard_content(self, content):
        """
        Add a piece of clipboard content to our history.

        This will also trigger our scribe (save_history) to record the change.
        """
        self.clipboard_history.append(content)
        self.save_history()

    def get_history(self):
        """
        Return our entire clipboard history.

        Sometimes, we need a stroll down memory lane...
        """
        return self.clipboard_history


# Command Line Interface (CLI)
if __name__ == "__main__":
    # Instantiate our super Clipboard History manager, and read any existing history.
    clip_hist = ClipboardHistory()
    clip_hist.load_history()

    if len(sys.argv) > 1:
        # If the script is called with arguments, we'll add those to history.
        clip_content = ' '.join(sys.argv[1:])
        clip_hist.add_clipboard_content(clip_content)
    else:
        # If there are no arguments, we'll print out the history.
        for item in clip_hist.get_history():
            print(item)

"""
There you have it! Our CLI-friendly, portable, Python-only, Internet-free Clipboard History!

Hope you enjoyed this journey as much as I did!
"""

Please note that this solution doesn't listen to the clipboard in real-time to store its history due to limitations in Python's standard library. Instead, it works by adding text to history when the script is called with arguments, and retrieves the history when it is invoked without arguments.