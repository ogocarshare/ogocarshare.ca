#!/usr/bin/env python
import os
import sys
import venv

if venv.sys.prefix == venv.sys.base_prefix:
    sys.exit("\nError: please run activate the virtualenv first.\n")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ogo.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
