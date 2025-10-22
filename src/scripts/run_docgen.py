import os
import subprocess

APPS = [
    "scraper",
]


def main():
    """
    Runs the docgen.py script for a predefined list of applications.
    """
    script_path = "src/scripts/docgen.py"
    base_path = "/Users/ankitranjan/Work/applications/src/universal_mcp/applications"

    for app in APPS:
        app_path = os.path.join(base_path, app, "app.py")
        command = ["python", script_path, app_path]

        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError:
            pass
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    main()
