#!/usr/bin/env python3
"""
HorseAI Launcher
----------------
Small terminal-based launcher: detects .html files in the folder,
lets you choose which one to serve, and opens it in your browser.

Usage:
    python3 serve.py                # interactive menu
    python3 serve.py source.html    # launch directly, no prompt
    python3 serve.py --port 8000
"""
import argparse
import http.server
import socketserver
import webbrowser
import os
import sys

BANNER = r"""
 _   _                    _    ___
| | | | ___  _ __ ___  ___/ \  |_ _|
| |_| |/ _ \| '__/ __|/ _ \ _ \ | |
|  _  | (_) | |  \__ \  __/ ___ \| |
|_| |_|\___/|_|  |___/\___\_/ \_\___|

        HorseAI · Local Launcher
"""

def find_html_files(directory):
    return sorted(f for f in os.listdir(directory) if f.lower().endswith(".html"))

def choose_file(files):
    # Kept for compatibility, but no longer used
    print(BANNER)
    if not files:
        print("No .html files were found in this folder.")
        sys.exit(1)

    print("Which file would you like to launch?\n")
    for i, f in enumerate(files, start=1):
        print(f"  [{i}] {f}")
    print()

    while True:
        choice = input("Choose a number (Enter = 1): ").strip()
        if choice == "":
            return files[0]
        if choice.isdigit() and 1 <= int(choice) <= len(files):
            return files[int(choice) - 1]
        print("Invalid option, please try again.")

def main():
    parser = argparse.ArgumentParser(description="HorseAI Launcher: serve a local HTML file")
    parser.add_argument("file", nargs="?", help="HTML file to open (if omitted, the first one is used)")
    parser.add_argument("--port", type=int, default=5500, help="Port (default: 5500)")
    parser.add_argument("--dir", default=".", help="Directory to serve (default: current directory)")
    args = parser.parse_args()

    os.chdir(args.dir)

    # Always show the banner so you know the launcher started
    print(BANNER)

    target = args.file
    if not target:
        # No argument: automatically serve the first .html file
        files = find_html_files(".")
        if not files:
            print("❌ No .html files were found in this folder.")
            sys.exit(1)
        target = files[0]
        print(f"▶ Automatically serving: {target}")
    elif not os.path.isfile(target):
        print(f"❌ '{target}' was not found in this folder.")
        sys.exit(1)
    else:
        print(f"▶ Serving: {target}")

    class Handler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
            super().end_headers()

        def log_message(self, fmt, *a):
            pass  # Suppress request logs for a cleaner output

    try:
        with socketserver.TCPServer(("127.0.0.1", args.port), Handler) as httpd:
            url = f"http://127.0.0.1:{args.port}/{target}"
            print(f"\n🐴 HorseAI running at {url}")
            print("   (Press Ctrl+C to stop)\n")
            webbrowser.open(url)
            httpd.serve_forever()
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {args.port} is already in use. Try another one with --port <number>.")
        else:
            print(f"❌ Failed to start the server: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nServer stopped. See you next time! 👋")

if __name__ == "__main__":
    main()
