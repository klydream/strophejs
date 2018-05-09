#!/usr/bin/env python
from django.core.management import execute_from_command_line
import sys
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attach.settings")
    execute_from_command_line(sys.argv)