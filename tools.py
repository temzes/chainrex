# TOOLS
import sys
import os

# EXTRA
sys.dont_write_bytecode = True

# MAIN
def main(settings: str):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as execute:
        raise ImportError("Could not import Django") from execute
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main(settings="settings.config")
